import cv2
import numpy as np
cap = cv2.VideoCapture("video3.mp4")

max_frame=cap.get(cv2.CAP_PROP_FRAME_COUNT)
#print(max_frame)
for frame in range(int(max_frame)):

  ret, img = cap.read()
  #print(frame%1==0)
  if(frame%3==0):
    #print(frame)
    #青のみ取り出す
    # BGRからHSVに変換
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.inRange(hsv_image, (66, 123, 6), (80, 230, 100))

    #gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #二値化
    #ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    #ブロブ検出
    n, img_label, data, center = cv2.connectedComponentsWithStats(gray)

    # (5) 検出結果の整理
    detected_obj = list() # 検出結果の格納先
    img_trans_marked = img.copy()
    for i in range(1,n):
      x, y, w, h, size = data[i]
      if size < 50 : # 面積300px未満は無視
        #print("見つからない！")

        continue
  
      # 確認
      cv2.rectangle(img_trans_marked, (x,y), (x+w,y+h),(0,255,0),2)
      cv2.circle(img_trans_marked, (int(center[i][0]),int(center[i][1])),5,(0,0,255),-1)
      #座標を書き込み
      cv2.putText(img_trans_marked, str((int(x+w/2),int(y+h/2))), (int(x+w/2),int(y+h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)
      print(frame,str((int(x+w/2))))
      cv2.imshow('img_trans_marked', img_trans_marked)
      #cv2.imshow('img_trans_marked', img_trans_marked)
      cv2.waitKey(0)
      break

