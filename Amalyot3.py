# 11. BIR NECHTA SHARTLARNI TEKSHIRISH

#          AMALYOT

#1.Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

    # Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("Iltimos, juft son kiriting: "))
# if son % 2 == 0:
# 		print("Rahmat!")
# else:
# 		print("Bu son juft emas")	
  
# # 2. Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

#     # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul

#     # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm

#     # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingiz nechida? "))
# if yosh < 4 or yosh > 60:
# 		print("Sizga muzeyga kirish bepul!")
# elif yosh < 18:
# 		print("Sizga muzeyga kirish 10000 so'm")
# else:
# 		print("Sizga muzeyga kirish 20000 so'm")

# # 3. Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# if son1 == son2:
# 		print(f"{son1}=={son2}")
# elif son1 > son2:
# 		print(f"{son1}>{son2}")
# else:
# 		print(f"{son1}<{son2}")

# # 4.    mahsulotlar degan ro'yxat yasang va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring. 

# mahsulotlar = ['un', 'yog', 'shakar', 'tuz', 'kartoshka', 'piyoz', 'sabzi', 'olma', 'banan', 'apelsin']
# savat = []
# print("Savatga 5 ta mahsulot kiriting:")
# for n in range(5):
# 	mahsulot = input(f"{n+1}-mahsulot: ")
# 	savat.append(mahsulot)		
# for mahsulot in savat:
# 	if mahsulot in mahsulotlar:
# 		print(f"do'konimizda {mahsulot} bor")
# 	else:
# 		print(f"do'konimizda {mahsulot} yo'q")	

# # 5.     Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['un', 'yog', 'shakar', 'tuz', 'kartoshka', 'piyoz', 'sabzi', 'olma', 'banan', 'apelsin']
# savat = []
# print("Savatga 5 ta mahsulot kiriting:")
# for n in range(5):
# 	mahsulot = input(f"{n+1}-mahsulot: ")
# 	savat.append(mahsulot)		
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
# 	if mahsulot in mahsulotlar:
# 		bor_mahsulotlar.append(mahsulot)
# 	else:
# 		mavjud_emas.append(mahsulot)	
# if mavjud_emas:
# 	print("Quyidagi mahsulotlar do'konimizda yo'q:")
# 	for mahsulot in mavjud_emas:
# 		print(mahsulot)
# else:
# 	print("Siz so'ragan barcha mahsulotlar do'konimizda bor")		
 
# 6.     foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ['ali', 'vali', 'hasan', 'husan', 'olim']
# login = input("Yangi login tanlang: ")
# if login.lower() in foydalanuvchilar:
# 		print("Login band, yangi login tanlang!")
# else:
# 		print("Xush kelibsiz, foydalanuvchi!")	
  
# 7.    Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.  

son = int(input("Biror butun son kiriting: "))
for n in range(2, 11):
		if son % n == 0:
				print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
