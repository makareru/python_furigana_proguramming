"""1月３日"""
"""print文でコンソール画面に表示する"""

# print("ハロー！")

# print(10+5)

# print(10-5)

# print(10*5)

# print(10/5)


# print("ハロー！",10+5, 10-5)

# a=10+5
# b=10-5

# print("ハロー！\n")

# print("aは{}\nbは{}です".format(a,b))

# c=10*5
# d=10/5

# print("cは{}\ndは{}で\n合計")

"""下記のコードはエラーになります（文字列と数字の結合はプラスではなく　カンマ区切り"""

# print("ハロー！"　+10+5,10-5)


"""下記は数字の計算と出力結果、文字列の結合と出力結果です"""

# print(int(2)+float(0.5),str(4.8)+str("です"))


"""変数textを定義した後、isdigit()で判定し整数が入力されるまでfalseの間ループさせる"""
# text="ハロー！"
# print(text)

# text=""

# while text.isdigit() ==False:

#     text=input("整数を入力して下さい")

#     if text.isdigit():
#         print("{}は整数です\nこれで終了します".format(text))
#         break
#     else:
#         print("{}は整数または数字ではありません\nもう一度やり直してください".format(text)) 


# print("ハロー！",10,3.5)

"""文字列の"Hallo"のHの文字をJに置き換えする。予約語.replaceで置き換えたのちに変数textの内容を表示するプログラム"""

# text="Hello".replace("H","J")
# print(text)


# text = input("入力せよ")

# if text.isdigit():
#     print(int(text)*1.08)
# else:
#     print("数字ではない")


"""変数に数値を割り当てる際には""でくくる"。"ans.isdigit()は内容ではなく"ans"と言う文字列の判定"""

# ans="456"

# print("123".isdigit())

# print(ans)

# print("ans".isdigit())

# print("ansの値は{}でans.isdigit()は{}です".format(ans,ans.isdigit()))


# print(4<5)

# print(6<5)


"""年齢別表示を条件分で分岐（キーボード入力による条件分岐）"""

# text=input("年齢は")

# age=int(text)

# if age<20:
#     print("未成年")

# elif age<40:
#     print("成人")30

# elif age<60:
#     print("老人")

# elif age<80:
#     print("死人")   

"""値だけの曜日を表示する"""

# wdays=["月,""火","水","木","金",]

# wdays2[月,火,水,木,金]

# nums=["1","2","3","4","5"]

# nums2=[1,2,3,4,5]

# print(wdays[1])

# print(wdays2[2])

# print(nums[3])

# print(nums2[4])


# print(wdays[1])

# print(nums[3])

# wdays=["月","火","水","木","金"]



# for day in wdays:
#     print(day,"曜日")

# for cnt in range(1,11):
#     print(cnt,"回目のハロー！")

# for cnt1 in range(1,10):
#     for cnt2 in range(1,10):
#         # print(cnt*cnt2)
#         print("{}×{}={}です".format(cnt1,cnt2,cnt1*cnt2))

# shikin=50000

# def a(shikin):
#     print(shikin)
#     shikin=shikin-5080
#     return shikin

# while shikin >=0:
#     # print(shikin)
#     # shikin=shikin-5080
#     a(shikin)
     
# team=["A","B","C","D","E"]

# opps=["A","B","C","D","E"]

# for t1 in team:
#     opps.remove(t1)
#     for t2 in opps:
#         print(t1,"vs",t2)

# def create_mail(recv,bill):
#     tmp="""{}様
#     PT企画の斎藤です。
#     今月の請求額は{}円です。"""
                      
#     msg=tmp.format(recv,bill) 
#     print(msg)

#  create_mail("山本",40000)
   
# def create_mail(recv,bill):

# print("{}様\n PT企画の斎藤です。\n　今月の請求書は{}です。".format(recv,bill))

# create_mail("山本", 40000)

"""関数による計算と出力（culcは個別計算・culc1は条件を満たす間反復計算。culc2は２つの引数がもつ値を表示"""
shikin=0

# def culc(shikin):
#     print("culcの値は{}です".format(shikin))
#     shikin=shikin-5080
#     print("culcの値は{}です".format(shikin))

# def culu1(shikin):
#     while shikin >=0:
#         print(shikin) 
#         shikin=shikin-5080
#         print("culu1の値は{}です".format(shikin)) 

# def culu2(shikin,result):
#     while shikin >=0:
#         result=shikin /2
#         print("shikin{}の半分は{}です。".format(shikin,result))
#         shikin=shikin-5080

# culc(50000) 

"""add_chargeに-1000を入れるとif文でreutnr 0が返され、1000を入れると　return int(bill*1.07)の"""

# def add_charge(bill):
#     if bill <0:
#         return 0

#     return int(bill * 1.07) 

# print(add_charge(-1000))

# print(add_charge(1000))

"""datetimeモジュール（module)を読み込んでcurに対応する曜日(youbi)を表示させる"""
# from datetime import date, timedelta
# youbi="月火水木金土日"
# start=date(2018,6,18)
# for d in range(14):
#     cur=start + timedelta(days=d)
#     wd=cur.weekday()
#     print(cur,youbi[wd])
"""sample.txtの内容を出力する前に、replaceで置き換えてコンソール表示して"""
# rfile=open("users/user/desktop/sample.txt",encoding = "utf-8")
# text=rfile.read()
# rfile.close()

# text=text.replace("まいご","らーめんおやぢ")
# print(text)

# wfile=open("output.txt",mode="w",encoding="utf-8")
# wfile.write(text)
# wfile.close()
"""ファイルわ読み込みこんでその中いあるforという文字列の数をfulepathと共に表示"""
# from pathlib import Path

# path=Path()

# count=0

# for filepath in path.glob("*.py"):

#     rfile = open(filepath,encoding="utf-8")

#     # print(filepath)
#     # rfile=open(filepath, encoding="utf-8")
#     text=rfile.read()
#     rfile.close()

#     cnt = text.count("for")

#     print(filepath,cnt+1)

#     cnunt += 1
# print("このフォルダ内の.pyファイルの数（countの値)は{}です" .format(count))   

from pathlid import Path

terms = { "for" :0, "if" :0, "else" :0 }

path = Path()

for filepath in path.glob("*.py"):

    rfile = open( filepath,encoding="utf-8")

    text = rfile.read()

    rfile.close()

    for term in terms:

        cnt = text.count(term)

        terms[term] += cnt

print(terms)        