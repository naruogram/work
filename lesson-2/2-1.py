SOC=["Hijikata", "Dannoue", "Matsubara", "Ishizaki", "Ura", "Miyahara", "Ueda",
     "Arisaka", "Inamoto", "Naruse", "Ikebe", "Uesaka", "Ikemoto", "Muranaka"]
# ２．上記で作成した変数SOCに，Chihara, Kumadaを追加せよ．追加後，リストの内容を確認せよ．
SOC.append("Chihara")
SOC.append("Kumada")
print(SOC)
# ３．上記の変数SOCから，Hijikataを削除せよ．削除後，リストの内容を確認せよ
SOC.remove("Hijikata")
print(SOC)
# ４．SOCのリストをアルファベット順で並べ替えよ．並べ替え後，リストの内容を確認せよ．
SOC.sort()
print(SOC)
# 性別判定(性別の情報がないので、適当に情報を与える)
str1=f"Mr.{SOC[0]}"
str2=f"Ms.{SOC[1]}"
str3=f"Mr.{SOC[2]}"
str4=f"Ms.{SOC[3]}"
str5=f"Ms.{SOC[4]}"
str6=f"Mr.{SOC[5]}"
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)