import streamlit as st
import io
from PIL import Image, ImageDraw, ImageFont


st.set_page_config(page_title="CodeWave Hub: Hacktoberfest Certificates", page_icon=None,
                   layout="centered", initial_sidebar_state="collapsed", menu_items=None)


background = Image.open("./banner.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=True)

#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

#1123, 794

events_data = {
    "Day 1": ["Abdul Baseer Ali Adeeb ", "Abdul Hafeez", "Abdul Mateen Khan", "Abdul Matheen", "Abdul Muqtadir", "Abdul Muqtadir ", "Abdul Rahman Khan", "Abdul Riyan", "Abdul Shakoor Kamran", "Abdullah Ali KHAN ", "Abs samad", "Aditya Pathak", "Adnan Ahmed Khan ", "Afeefulluqman", "Afnan Qureshi", "Ahmed Rafi Farooqui ", "Akhilesh Reddy Patlolla", "Alvira", "Alyssa Gwyn Donor", "Amaan Khan", "Amair Mohd Khan", "Ameena Firdous ", "Ameena Unissa", "Amer Anus", "Arsalaan raza", "Asfiya ", "Atanshu Ahlawat", "Ayesha Javeed", "Ayesha Siddiqua ", "Ayman Maboob Shaik", "B.mahesh babu", "Bhukya Shiva Nayak ", "Dhruv Pridhnani ", "Dinesh Nalam", "dudekula sohel", "Gavvala Sai Venkata Vikram Aditya ", "Habeeb Saad", "Hafsa", "Iqra Fatima ", "Ishaq Ahmed ", "Jaweed", "Jinitangsu Das", "Kafia Kauser", "Karthik Samala", "Koushik Pyarasani ", "Lakshya", "Lode Sai Charan", "Madiha sultana", "Mahidhar Damera", "Maviya Sannan", "Max Alliance", "Md Abdul Raheem Khan", "Md Abdul Wajid", "Md azeem", "Md Ibrahim Zain ", "Md Motiour Rahman ", "Md Rayyan Nawaz", "Md Toufeeq Uddin", "Md Ubaid Ur Rahman", "Md. Muqtadir Quadri ", "MDABDUR RAHMAN MAQSOOD ", "Mehveen Fatima", "Mir Ahmed Ali", "Mirza Danish Baig ", "Mirza Hyder", "Mirza Mubashir Baig", "MOHAMAMD RIZWAN", "Mohammad Abdul Khaliq", "Mohammad Anwar Uddin", "Mohammad Danish", "Mohammad Danish Ali Khan", "Mohammad Fawaz Ali Quadri ", "Mohammad Zaki Uz Zama", "Mohammed Abdul Ahad ", "Mohammed Abdul Hameed ", "Mohammed Abdul Qavi ", "Mohammed Abdul Shoaib Hilal", "Mohammed Aleemuddin Ahmed ", "Mohammed Amaan Uddin ", "Mohammed Ammar", "Mohammed Asif", "Mohammed Asim", "Mohammed Ayaan khan ", "Mohammed Faisal parvez", "Mohammed Fakhrudiin ", "Mohammed Faseehuddin", "Mohammed Fouzaan Hussain", "Mohammed ibrahim ", "Mohammed Islamul Haq ", "Mohammed Islamul Haq ", "Mohammed Masood Sharief ", "Mohammed Mudaser", "Mohammed Muqsith Ali Khan", "Mohammed Mustafa ", "Mohammed Mutahir Hussain", "Mohammed Nawaz khadar qasimi", "Mohammed Omer Mohammed Abdullah Batouk ", "Mohammed Omer Mohammed Abdullah Batouk ", "Mohammed Salahuddin", "Mohammed Shouraim Ahmed ", "Mohammed Sufiyan", "mohammed ufraan abdullah siddiqui", "Mohammed Wahaj Abdul Salam", "Mohd Abdul Aleem", "Mohd Abdul Malik ", "Mohd Abdul Sami ", "Mohd Ghouse Tazeem", "Mohd Irfan", "Mohd Najeeb Murtuza", "Mohd Rayaan Uddin ", "Mohd rehan", "Mohd Siddiq", "Mudassir", "Mudassir Ullah Khan Mohammed", "Muhammad Affan Asif", "Muhammed Muzzammil", "Muhathir Talha Habeeb", "Muntazir Mehdi Ali", "Muskan Begum", "Omer Ahmed Quadri ", "Padala Shiva Sai kiran ", "Pradeep ", "Rahul Panchal", "Raiyan Ali", "Rayyan", "Rida Baquri", "Rida Khan", "Ruha fatema", "Sadia ", "Sadia Ilahi", "sai shankar", "Saikumar Mangilipelly", "Samiuddin Ansari", "Samiuddin Ansari", "Samiya anam", "Samrien erum ", "Sathwika manda", "SHAIK ABDUL ATEEQ ", "SHAIK ABDUL KALEEM", "Shaik Anas", "Shaik Mahboob Mohiuddin ", "Shravan Lingampally", "Siddhanth Rathod", "Siddhrajsinh Ranjitsinh Gohil", "Siraj Malik", "Sneha ", "Suhaib", "Suhaib Ahmed ", "Syed Abdul Muddassir ", "Syed Ibrahim Nazeer", "Syed Moazam", "Syed Mudabbir Uddin ", "Syed Muzammil", "syed omer", "Syed Omer Shah", "Syed Salman Jalal", "Syed Shafaq Hussain ", "Syed Siddiq Ahmed", "Syed Zabiulla Hussaini", "Syeda Aamina Bushra", "Syeda Juwairiya Fatima", "Syeda Taahaa Farhath ", "Tabassum Begum ", "Tahniyath Fathima", "Tauqeer", "Thaizia", "Tiruveedula Manas Chakravarty", "Vayunandan", "Wasee", "Yahiya ", "Yusharth Singh", "Zohair shahid khan ", "Zufaiar aslam"],
    "Day 2": ["Aamina", "Abdul shakoor kamran", "ABDULLAH ALI KHAN", "Affaan Jaweed", "Amaan Khan", "Amair Mohd khan", "Ameena Unissa", "Amer Anus", "Asfiya", "Dawood khan ", "Dudekula Sohel", "Gavvala Sai Venkata Vikram Aditya ", "Hafsa", "Iqra Fatima", "Jinitangsu das", "Kafia Kauser", "Kamil kaif", "Lakshya ", "Madiha Sultana", "Md Abdul Malik ", "md abdul wajid", "Md Ibrahim Zain", "Md Motiour Rahman ", "Misbah ullah", "MOHAMMAD ANWARUDDIN", "Mohammad Danish", "Mohammed Abdul Ahad", "Mohammed Abdul Khaliq", "Mohammed Abdul Qavi ", "Mohammed Abdul Shoaib Hilal", "mohammed abdur rahaman maqsood", "Mohammed abdus samad", "Mohammed Ammar", "Mohammed fahad Khan ", "Mohammed fahad Khan ", "Mohammed fardin khan", "Mohammed Islamul Haq ", "MOHAMMED MAVIYA SANNAN", "Mohammed Muzammil Ahmed", "Mohammed Nawaz Khadar Qasimi", "Mohammed Omer Mohammed Abdullah Batouk ", "Mohammed Salahuddin", "Mohammed Shouraim Ahmed ", "Mohammed Shouraim Ahmed ", "Mohammed Ufraan", "Mohammed Wahaj Abdul Salam ", "Mohd Abdul sami ", "Mohd Najeeb Murtuza ", "Mohd Siddiq ", "Muhammad abdul raheem khan", "muhammed habeebuddin muzammil", "Muskan begum", "Rayaan uddin Haqqani", "Rehan", "Rehan", "Rida khan", "Ruha.fatema", "samiya anam", "Sania Mohammadi", "SHAIK ABDUL KALEEM", "Syed Abdul Razzaq ", "Syed Ibrahim Nazeer ", "syed inzamam", "Syed Mudabbir Uddin", "Syed Omer Shah", "Syed Siddiq Ahmed", "SYEDA AAMINA BUSHRA", "Tabassum Begum ", "Thaizia", "Zohair Shahid Khan"]
    
}


#W, H = (1123, 794)


#api = "https://api.npoint.io/0ac056978990354196e5"

A = "./day1.png"
B = "./day2.png"
# options = []
# for i in names.keys():
#     options.append(i)

font = ImageFont.truetype("Poppins-Medium.ttf", 100)
events = st.selectbox("Select", events_data.keys())
name = st.selectbox(
    "Select your name for generating certificate", events_data[events])
name = name.title()
if events=="Day 1":
    im = Image.open(A)
else:
    im = Image.open(B)

d = ImageDraw.Draw(im)

W, H = im.size
w, h = d.textsize(name, font=font)
e_w, e_h = d.textsize(events, font=font)
print(w, h)
d.text(((((W-w)/2) + 105, ((H - h)/2) + 350)),
       name, fill=(56, 56, 56), font=font)
d.text(((((W-e_w)/2) - 850, ((H - e_h)/2) + 580)),
       events, fill=(56, 56, 56), font=font)
if st.button("Get Certificate"):
    ioData = io.BytesIO()
    im.save(ioData, format='PNG', quality='keep')
    finalImage = ioData.getvalue()
    st.image(finalImage)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
