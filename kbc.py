#  It is exercise 2 kon banega roadpati?

print('Hello,Mr. Welcome to the Kon banega road-pati\n')
name =input( 'What is your name? : ')                          
print('Mr.',name,'Kya aap such me road-pati banna chahte hain?\n'  )
start_game = input('a) Yes   b) No ,\n choose your option a or b : ')

if(start_game=='a'):
    print('Ok Ok, Very Bad\n')

    print('**********Instruction**********\n 1) Game start karne ke liye aapki per/year income  80,000 INR, Hone chahiae.\n 2)  80k/per year se jyada  Hone pe ham aapko balcklist kar denge. \n Alert=> Dhyan Rakhna Sahi jawaab dene pe kangaal bi ho skte hain...\n ')
    inr_to_startGame = int(input('Q- Aap ki per year income kya hai ?\n', ))
    if(inr_to_startGame <= 80000 ):
        print('Good , Aapka hi intjaar tha...\n')
        print('Chalo Game start karen...\n')
        questions =[]

    else:
        print('Aap Game khelne layak hi nahi hain , Ameer aadmi kahinka...\n')



else:
    print('God job , Yahan kyu aaye ho ?? \n Jaao insta pe ye linkdin Shorts scroll karo')