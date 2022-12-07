import streamlit as st
import io
from PIL import Image, ImageDraw, ImageFont


st.set_page_config(page_title="Consortium Certification", page_icon=None,
                   layout="centered", initial_sidebar_state="collapsed", menu_items=None)


background = Image.open("./new_banner.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=True)

#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

#1123, 794

events_data = {
    "AMC Antariksh Competition": [
        "Team Knight angel ",
        "Team ZAKK",
        "Team Tactical Takeoff",
        "Team RABS GLIDER ",
        "Team Big Guff",
        "Team KNIGHT ANGEL",
        "Team Fly High",
        "Team _*Dothraki Crew*_",
        "Team Awesome dynamos",
        "Team Amateur Engineers",
        "Team THE CHOSEN ONES ",
        "Team Awesome dynamos ",
        "Team Chronicles ",
        "Team Aero bros",
        "Team The Wright Brothers ",
        "Team Musaab ",
        "Team VC",
        "Team GARUDAS"
    ],
    "Battlegrounds CAD": [
        "Y Sachin",
        "S.Shiva Rama Krishna",
        "P. Varshini",
        "Talla Vivek",
        "B SHARAN KUMAR",
        "Kakkirala Venkatesh",
        "Kurapati vinay",
        "Vadkapuram ajay",
        "K AKSHAY KUMAR",
        "VELDANDIVARUN",
        "Bheemshetty Kushal",
        "Tanneru brahmaji",
        "S.Maneeshwar Reddy",
        "Nadirge Chandravadan",
        "Kokkonda Abhishek"
    ],
    "Buckers": [
        "B. Sai Vamsi Karthik",
        "Saketh",
        "Shivani",
        "Nikitha",
        "Ch.Sai Rahul",
        "K.Sandeep Reddy",
        "P.Shivamani",
        "Uday Sharma",
        "Maheshwari",
        "Meghana",
        "Meghanath",
        "Priyanka",
        "Shyam srinivas",
        "NIKHIL KOLUGURI",
        "SHASHANK MANDALA",
        "NAVEEN MAALE",
        "S.Gayathri",
        "sk.Karishma",
        "M.Rahul",
        "S.Rithesh",
        "Aishwarya",
        "Rashmika",
        "Srihitha",
        "Sriraj",
        "Prashanth Sai Balaji Maguluri",
        "Sohail Ahmad",
        "Sai Varun",
        "Prachethan reddy",
        "M.V.Phaneendra",
        "Avinash netha",
        "Ramakrishna",
        "Uday shankar",
        "Pentela om Sri Sai sahasra",
        "Katarapu Roney Moon",
        "Sai Anjana Perepi",
        "Pavan Bejadi",
        "Raghavendra reddy",
        "Saikumar",
        "Shruthy",
        "Veechika",
        "Manisha",
        "Shruthi",
        "Swarani",
        "Aaditya Santhosh Nallah",
        "Chandra Shekhar",
        "Jagadeesh",
        "Revanth",
        "krupa",
        "Alekhya",
        "Vedakshari",
        "D.subrotho chakravarty",
        "Shahisnu Manohar",
        "Deeptangshu Banik",
        "Tummala Depak",
        "Dharvik",
        "Bhuvneshwar",
        "Ansik",
        "K.MANI KUMAR",
        "A.Manikyam",
        "D. Ashish",
        "Ankith thakre",
        "A SAI DURGA PRASAD",
        "P SANDEEP",
        "RAHUL",
        "J VISHAL",
        "Kishan Agarwal",
        "Jaideep Sai",
        "Vaibhav",
        "Devesh",
        "A Shishir",
        "S.TEJASWI",
        "T.DIVYA",
        "Y.GEETHA SUSHMITHA",
        "T.NAVEEN",
        "M.GOPI KRISHNA",
        "S.ADITHYA"
    ],
    "Clue Mining": [
        "S.Sakthi Priyan",
        "MD AMEESHA",
        "KAUSHIK",
        "G.Eshwar",
        "B.Harshini",
        "Nehal",
        "B.Pranavi",
        "K. Prashanth",
        "sanjana jade",
        "Prasanna",
        "K P Reddy Kumar",
        "Pavithra",
        "Shaik.karishma",
        "Narsimha reddy",
        "Srujan reddy",
        "Naveen kumar",
        "Sai Praneeth",
        "Raghavendra reddy",
        "N NIKHIL",
        "M.Sathish kumar",
        "Khagesh Kumar",
        "Sujitha Jammula",
        "Neeraj Kumar",
        "Ch pavan kumar",
        "Hasini",
        "Narrasahithi",
        "Nissy Jillella",
        "Amaan khan",
        "Sriraj",
        "B sathwik",
        "sai santhosh",
        "Jashwanth reddy alla",
        "T.Nikhil varma",
        "Sravya",
        "Nikhil koluguri",
        "G Hemanth Venkata Reddy",
        "M Chinmai",
        "Sanskruthi",
        "Akshitha",
        "Sneha kancharla",
        "Sameem haque"
    ],
    "Enigma": [
        "Sowmya Siddanki",
        "Vaishno Phaneesha",
        "Thejaswi",
        "S.Sakthi Priyan",
        "Sonu Reddy Surakanti",
        "Asma Begum",
        "Krishna Durga Devi",
        "Choprala Anjani Varshitha",
        "Madupu Hema",
        "A.Saikumar",
        "A.Vishal",
        "Vignesh",
        "Gautam",
        "Phanesh",
        "Lekhaj",
        "Shiva Krishna",
        "Sai Srujan",
        "Narasimha",
        "Vinay",
        "Vivek kasala",
        "Anthony Vishal",
        "Sai Varshini",
        "Sahithi",
        "Joel",
        "Rohit Joy",
        "Vishnu",
        "Thanuja",
        "Nikhil",
        "Shashank",
        "Mounika",
        "Sushma",
        "Sarvani",
        "Padmavathi",
        "Akhila",
        "Hasini",
        "Sriya Pranathi",
        "Jahnavi",
        "Nikitha",
        "Viharika",
        "Deepak",
        "Adithya",
        "Aashrita Reddy",
        "V. Manogna",
        "Keshav",
        "Jashwanth",
        "Roshitha",
        "Nitisha",
        "S.D. Vaishnavi",
        "Shreya",
        "Jayanth",
        "Aslam",
        "Pujita Krishnan",
        "Zameera",
        "Nayana",
        "Navya",
        "Indu",
        "Varshini",
        "Adnaan",
        "Arun",
        "Adarsh",
        "Navateja",
        "VARSHITHREDDY",
        "Bhavani Shankar",
        "Rahul",
        "Siddu",
        "Rahul",
        "Pradeep",
        "Sanjana",
        "Manasa",
        "Sai jishnu",
        "Revanth",
        "Madhulatha",
        "Sanjana",
        "Krupa",
        "Bhargav",
        "Gayatri",
        "Akshaya",
        "Nilesh",
        "Adithya",
        "Tejaswini",
        "Tejaswi"
    ],
    "Filmlet": [
        "Team Bhaagavatham",
        "Team Rockers",
        "Team Inevitables",
        "Team Epic Failures",
        "Team Nasha ",
        "Team Kanya Rashi",
        "Team Charan",
        "Team First Film"
    ],
    "Grand Lens": [
        "A.CHAITANYA RAGHAVA",
        "LINGALA AJAY",
        "Pradarshan Raj",
        "K P Reddy  Kumar",
        "Jarupala Pavithra ",
        "CH.PAVITHRA",
        "S.javahar reddy",
        "SUNKIREDDY JAVAHAR REDDY",
        "Kodalwar prashanth",
        "G.NehaReddy",
        "G Praveen Kumar ",
        "Sai Varshith Munigeti ",
        "BATTUWAR VISHNU",
        "T. Abhay sai",
        "B.MAHESH",
        "N.Srinidhi",
        "B.MAHESH",
        "BATTUWAR VISHNU",
        "Rekhawar Vivek",
        "Shaik Farhatunnisa",
        "Palapati Veda Vaishnavi",
        "chandu kumar",
        "ABHILASH DAVARASINGI",
        "Ajay reddy ",
        "Suchismithaaa ",
        "Priyanandini",
        "GUMMADI CHARAN ",
        "Gummadi Charan ",
        "gayathri",
        "Abhiram Choudhary B ",
        "Uday Prakash ",
        "P.Durga Harshith",
        "P.Durga Harshith",
        "Samuel james",
        "Lingala Amulya",
        "Reeha Thouheed ",
        "THOTA ASMITHA",
        "G.Abhiram ",
        "Abhiram ",
        "Kirthi Reddy ",
        "Jahnavi Goli",
        "Samuel james",
        "Akhilperuri",
        "Nihithani",
        "Venkata Tarun Panangipalli",
        "Nature ",
        "Harshavardhan Reddy"
    ],
    "Innover 2K22": [
        "Vuppu Mahesh",
        "Mohammed Adhnan Mahboob",
        "Kowkutla Jeshwanth Reddy",
        "Gadala Naveen",
        "Umama Mahroz",
        "Puneetha Sutaram",
        "Shokat Ali",
        "Zulfiqar Ali",
        "Vinayak Kawle",
        "Manasa",
        "Vishwanth",
        "Akansha",
        "Anil Sai",
        "Pranay",
        "Praveen",
        "Sravan",
        "Preetham",
        "Kranthi",
        "Yashwanth Sannidhi1",
        "V Bhuvaneshwar",
        "P Prabhakar",
        "P Bhargav Reddy",
        "Manvitha",
        "SRIKANTH",
        "JYOTHI",
        "ABHIRAM",
        "Hemanth"
    ],
    "Now Learn Service Now": ["Gowtham Reddy"],
    "Prastuti": [
        "Naga Tanusri Nukala",
        "Myalkala Sai Sudhir",
        "Sandeep Kumar Yadav Vanguri",
        "Nara Adithya Raj",
        "Prashanth Suryavanshi",
        "B.Uday Kiran",
        "Maloth Shyam Prasad",
        "Roshni Kumari",
        "Iare",
        "Durga Lakshmi",
        "Mephie Marilyn",
        "Akanksha pathuri",
        "Vemula Deekshitha",
        "Pinjala Lohitha",
        "B. Jayanth kumar",
        "G.Shivani",
        "D.Sowmya",
        "B Naveen kumar",
        "St.peter",
        "Aarthi vanshette",
        "G.Alekya",
        "K. Vineela",
        "C Aparna",
        "Mlrit",
        "J KOUSHTHUBHA",
        "S pravalika",
        "D.vijaya lakshmi",
        "Govind raj",
        "P.siri",
        "G.jahnavi srija",
        "N Ajay",
        "D.Jatin",
        "C vishupriya",
        "K.harshitha",
        "Khara K Aryan",
        "P Prasuna",
        "G Rishika",
        "P sujay",
        "M sarayu",
        "Asmitha",
        "Bhavani",
        "Reeha",
        "Deepthi sai",
        "K.Paarth",
        "M muthaiah manideep",
        "Pathuri Rama krishna",
        "Dhara abhinav",
        "Mudimanchi pranay kumar",
        "Karri akansha reddy",
        "Suraram ravalika",
        "Dhappuri mohana",
        "Joohitha Vemulapalli",
        "Kavya Sree Kyanam",
        "Harshitha Allaka",
        "Pavani Thunga",
        "Ramavath hemavathi",
        "Muchintala gayathri",
        "Sangu amitha shree",
        "Nikitha Muthyala",
        "Rekha seervi",
        "Pulichintha Mythri",
        "B Paavani",
        "M . Rahul",
        "P. Dinesh Reddy",
        "Krishna Desai",
        "CH Praneeth",
        "B.Kiran",
        "Madhuri.P",
        "Dinesh B",
        "A.Pranathi",
        "L.Anjali",
        "K.Rishitha",
        "B.Ramya",
        "P.Uday kiran",
        "R.Pradeep",
        "T.Rajesh",
        "B.Bharath",
        "M.vardhan",
        "Mohan krishna",
        "Maddela Sai Dharani",
        "GOCHALAM VINOD",
        "Bhutham Sai Goutham",
        "Chenna Sai Raj",
        "Dappu Roshni",
        "Gande Shravyasri",
        "S.ritwik prakash reddy",
        "Nagarapu Sandeep",
        "Sk.Aquifa",
        "Sannutha vollu",
        "J sujitha",
        "N Rishi Priya",
        "S varshini",
        "T Deva",
        "M.Charitha",
        "M.Anuradha",
        "B.Renu Asritha",
        "Hemanth Yerra",
        "Varun",
        "Yashwanth",
        "M vishal",
        "Naresh",
        "Saipranaya Chepuri",
        "Keerthana Palaparthy",
        "Karanam Lakshmi Abhigyna",
        "Jignyasa gopalam",
        "Kathi Venkata Lokesh",
        "N Sai Sanjay Sharadvanth",
        "mohd shayaan Alam",
        "Dasari Suresh",
        "N.Sai Vardhan",
        "Jangam Varun",
        "Vidheesh Kumar Kasanagottu",
        "G.Tarun",
        "Mikkili Shiva Sai Reddy",
        "Matta Sannithraj",
        "Jay Krishna",
        "Ganga Hitesh",
        "Prudhvi Narayana",
        "Nithish",
        "Ganji Adithya"
    ],
    "Sethu - The Ally Forging": [
        "Peesari jyothi",
        "Nayak Narsimha",
        "Sunkari Sai pranith ",
        "Meesala Akshitha",
        "Mohammad Afroz",
        "Samuel Stephen",
        "Thanneeru kishore",
        "Mothkuri Rishith Goud",
        "Arkala Pavani Goud",
        "Beeravelli Anvitha Reddy",
        "Sanku Aravind ",
        "Kummari Ramesh Kumar",
        "Panthula Shravan kumar",
        "Y. Sachin",
        "Vivek Singh",
        "Durgam Abhinay",
        "Bathula Yamini",
        "Challa Dhanush",
        "Mohammad Afroz",
        "Konamoni Trisha",
        "Gadapa Rithesh ",
        "Choppari Naveen",
        "M Krishna Mohan"
    ],
    "Teens Den - BGMI": [
        "Nagapuri Sanjay",
        "Sk. Shaheed",
        "Shashidhar",
        "Sachin Kumar",
        "Shabda Prakash",
        "Vivek",
        "D. Thrinesh",
        "P. Yeshwanth",
        "Durga Harshith",
        "K. Tejith",
        "R. Hemanth",
        "Siddarth",
        "M. Koushik Reddy",
        "Nihal Saini",
        "T. Govind Raju",
        "S. Bhanu Prakash",
        "A. Chaitanya",
        "M. Bala Murali Krishna",
        "G. Dineeth",
        "M. Sai Prashanth",
        "S. Nileesh",
        "P. Nikhil",
        "E. Pranith",
        "M. Varun Josh",
        "Sree Praneeth Mohan",
        "Vinay Sai",
        "Vamsi Krishna",
        "Neeraj Kumar",
        "Mani Teja",
        "B.V. Raghu Ram",
        "Naga Babu",
        "Abhishek",
        "Stanly",
        "Uday Kiran",
        "Umesh Chandra",
        "G. Phani Kumar",
        "Shiva",
        "Durya",
        "Abhishek",
        "Akhil",
        "Akash",
        "Sunki Prudhvi",
        "Pranjal",
        "A. Sai Kumar",
        "Navanish",
        "Pavan Teja",
        "G. Hemanth Reddy",
        "P.G. Bharadwaj",
        "M. Chaitanya",
        "G. Vamshi",
        "A. Sidharth",
        "S. Morise Anthony",
        "Mohammed Amaan",
        "D. Sai Sandeep",
        "Charan",
        "Rahul",
        "Kowshik Avilala",
        "K. Pratham",
        "Pavan",
        "Charan",
        "Surendhar",
        "S. Vinod Kumar",
        "Surya Prabhas",
        "J. Sai Praneeth",
        "K. Nikhil",
        "B. Sharan Paul",
        "P. Saketh",
        "V. John Manoj",
        "R. Karthik",
        "C.S.Puneet Teja",
        "V. Sai Chaitanya",
        "A. Shanthan",
        "K. Manikanta",
        "O. Sai Kiran",
        "Sai Varma",
        "Nithin",
        "Mahendar",
        "A. Arun",
        "P. Venkateshwar Reddy",
        "A. Abhishek",
        "Sudheer",
        "Vishnu",
        "Karthik",
        "Rohan",
        "Bharath",
        "Phanindra",
        "Vinay",
        "Kamal",
        "Virat",
        "Sri Anjaneyam",
        "G. Sujay",
        "A. Harikrishna",
        "Ch. Sridarshan",
        "P. Uday Kiran",
        "J. Saketh",
        "R. Pradeep",
        "M. Rahul",
        "A. Paul Anurag",
        "H. Chaitanya",
        "B. Yashwanth",
        "B. Chandrashekar",
        "Dayanand",
        "Sharath Chandra",
        "Ch. Manoj",
        "Mohan Krishna",
        "Mohan Reddy",
        "Rajesh",
        "Praneeth",
        "K. Nithin Reddy",
        "D. Venkata Akhil",
        "T. Sumanth Naidu",
        "T. Hemanth Naidu",
        "M. Amruth Reddy",
        "T. Abhiram Reddy",
        "B. Abhiram Chowdary",
        "K. Chandu",
        "A. Karthik",
        "P. Aravind",
        "Rohan",
        "Sai Jai Kiran",
        "Charan",
        "Uday Kiran",
        "Mitesh",
        "Sujay",
        "Phaneesh",
        "Chandrashekar",
        "Sai Ashmit",
        "Mukesh"
    ],
    "Teens Den - Call of Duty": [
        "Saketh Sri Harsha",
        "M. Prabhas",
        "R. Shashank",
        "G. Lekhaj",
        "E. Surya Teja",
        "CH. Yugander",
        "J. Victor Paul",
        "G. Vivekananda",
        "CH. Manoj",
        "CP. Prakul",
        "Jaypreet Singh",
        "Vignesh",
        "Phaneesh",
        "Omprakash",
        "Keerthan",
        "Sagun varma",
        "Prasuna",
        "K sathwik",
        "Ramakanth",
        "Hruthi Vadan",
        "Varun",
        "T Sri Vaishnavi",
        "Rahul",
        "Sidharth S",
        "Sidharth A",
        "Umesh Chandra",
        "Sri Varsh",
        "Ashish Atkuri",
        "Jagpreeth Singh",
        "Manoj Kumar",
        "Bharath Arvapalli",
        "P. Prasana",
        "K. Sathvik",
        "S. Ramakanth",
        "Shaik Gouse",
        "Yakub samad",
        "Aman afridi",
        "Gouse madeena"
    ],
    "Teens Den - Free Fire": [
        "K. Shanmukh",
        "P. Sai Raghu Ram",
        "T. Rajesh",
        "M. Sharath Chandra",
        "Dindi Sai Swaroop",
        "T. Upender",
        "S. Vishwanath",
        "N. Sravan Kumar",
        "Pavan Tej",
        "Pavan Kumar",
        "Tyson",
        "Dino",
        "Rameez",
        "Soujith",
        "Bharat",
        "Bhargav",
        "N. Lavan Reddy",
        "Likhith",
        "K. Praneeth Rao",
        "Neeraj",
        "J. Meghanath Pavan Sai",
        "P. Karthik",
        "J. Karthik",
        "Mani Kumar",
        "Samir Chandra",
        "Hariteja",
        "Shivaram",
        "A. Goutham",
        "K. Sai Kumar",
        "Shiva",
        "Akhilesh",
        "Navaneeth",
        "P. Bipin",
        "Bhanu Prakash",
        "Deva Rugral",
        "R. Vamshi",
        "Sai Teja",
        "Lakan",
        "Pavan",
        "KP. Reddy Kumar",
        "A. Pranav Reddy",
        "V. Aravind",
        "Md. Shakeer",
        "V. Siddesh",
        "E. Rajkumar",
        "G. Shanmukesh",
        "B. Ranadheer",
        "B. Nitish Kumar",
        "Pradeep",
        "Charan",
        "Koushik",
        "Srikanth",
        "Vikhil",
        "Vinay",
        "Adithya",
        "H. Chaitanya",
        "G. Chaitanya",
        "B. Sathwik",
        "K. Sathvik",
        "P. Sai Srujan",
        "M. Kalyan Babu",
        "S. Sagun Varma",
        "P. Sai Charan Reddy",
        "P. Shashank Reddy",
        "B. Yuvaraju",
        "Ch. Mahananda Reddy",
        "M. Vishal",
        "R. Srinivas",
        "Y. Yashwanth",
        "Vamshi",
        "G. Kishor",
        "M.M.Manideep",
        "D. Abhinav",
        "K. Paarth",
        "Sai Bhargav",
        "Sai Kiran",
        "Mujaheed Ahmed",
        "Shashank Goud",
        "Nikhil",
        "J. Shiva",
        "G. Eshwar"
    ],
    "Teens Den - Online Chess": [
        "Maram Manoj Reddy",
        "Morise",
        "Harshaveer",
        "Mohammed Iyaz",
        "Sathish Kumar",
        "Rai Tejaswini",
        "Dara Tejaswi",
        "D. Thrinesh",
        "M. Vivek",
        "K. Aravind",
        "V. Abhinav",
        "P. Phanindra",
        "Prashanth",
        "T. Asmitha",
        "P. Datta Jagan",
        "K. Teja Arjun",
        "Szeevan Paul Raj",
        "M.K.B. Sudhindra",
        "Aniketh",
        "V. Faneendra",
        "K. Srikanth",
        "M. Srinivas",
        "Sirikonda Sai Vamsi",
        "M. Rishith Naga Srinivas",
        "M. Venkat Sumanth",
        "M. Sridhar",
        "M. Ashiesh",
        "M. Shashank Goud",
        "K. Nikhil",
        "Ankur Roy",
        "S. Mohan Reddy",
        "P.V. Srujan Reddy",
        "M. Santosh",
        "K. Arun Kumar",
        "G. Chakradhar"
    ],
    "TLE Hack": [
        "Narsimha reddy",
        "Abhijitha Kandukuri",
        "Katta Sreeja",
        "Bussa Varsha",
        "M. KARTHIKEYAN REDDY",
        "Vishnu Vardhan",
        "Harika Juturu",
        "P.Bhavya sri",
        "Vangaveti poojitha",
        "Sankranthi Bhuvaneswar",
        "Varshitha veeramalli",
        "Aishwariyaa Anand",
        "M.chinmai",
        "Abhighna Kilaparthi",
        "Sameera Bethapudi",
        "Maloth Ashwitha",
        "Satthu Harshitha Reddy",
        "Viharika kommula",
        "lingala kalyan",
        "Mudavath Sindhu",
        "T. Harshitha",
        "Guthi Deepthi Sarayu",
        "Keerthana madeshi",
        "Shine",
        "P Ranvanth Kalyan",
        "HAMANPURE VAIBHAV",
        "Madupu hema",
        "Matta Bala Shanmukh",
        "Ch.Anjani varshitha",
        "Aryan kiran gawade",
        "Seela Venkata Naga Devesh",
        "Adhikya",
        "NARALA SIDDHARTHA",
        "Gnaneshwarasairam indrala",
        "Bijji Sai Siddeshwar",
        "Pranathi Ageer",
        "Anirudh Datti",
        "Kishan Agarwal",
        "Raj kumar Rana",
        "Khirsagar Rishitha",
        "Bharadwaj Pemmaraju",
        "Sathwika Reddy Lekkala",
        "Arjun Mylagani",
        "Thota Anjusree",
        "Yerramshetty Dharvik",
        "Lingampally Anjali",
        "J. Shiva Vara Prasaad Reddy",
        "Balram Ramya",
        "Kanni Shashankh Vasudev",
        "ANASURI SAI KOUSHIK",
        "MITTAPALLI LOKANADH ASHIESH KUMAR",
        "Jignyasa Gopalam",
        "yuvaraju",
        "mahanadha",
        "Keerthana Palaparthy",
        "Pradeep",
        "ADABALA SREE PRANEETH MOHAN",
        "Mallik Narsina",
        "Ojaswini",
        "Anaparthy Rohit Joy",
        "Sudarshan Rao",
        "Vishnu Srivatsava",
        "Shashank Bhake",
        "P Sai Siddhardha",
        "M Bala Venkata Murali Krishna prasad",
        "KARANAM LAKSHMI ABHIGYNA",
        "Gondipali venkata dheeraj reddy",
        "Srujan sai voodarla",
        "Jayanth Bharadwaj",
        "Dheeraj",
        "Arandkar Vishal",
        "ASHISH PRADHAN",
        "Dirisam Joel Rayan Raj",
        "HIMAKAR",
        "Ashraf Mohammed",
        "B Bhanu Prakash",
        "Jithin",
        "Satya Srujan Akkineni",
        "T vinay kumar",
        "Patlolla mahesh Reddy",
        "c.hemanth chowdary",
        "Sai Shivani",
        "KRISHNA SAI NITHIN ALIMELLA",
        "GAMPA SRUJANKUMAR",
        "K.vivek",
        "Vangala sri sai prajeeth",
        "Manchikanti Nehanjali",
        "Jaidheer Naik",
        "GAYATHRI ANTERVEDI",
        "R.Vamshi",
        "K.Sri Harsha",
        "Madhurya",
        "NETHULA SHIRISHA",
        "ERRA SANKEERTH",
        "R.Sai Charan Reddy",
        "G Jashwanth Sai",
        "M.Thanuj",
        "B Nikhileshwar Reddy",
        "Rahul Munamarthi",
        "Rahul",
        "Om Gupta",
        "B sathwik",
        "Kondapalukula srinika",
        "A Sai Kiran",
        "Tarun Kotha",
        "Siva Ram Prasad Maddukuri",
        "Katla Shiva Kumar",
        "Archana chintapatla",
        "Paliwal Naresh",
        "Anvesh Ettaveeni",
        "Easari Surya Teja",
        "C.h Rohith kumar",
        "MEGAVATH RAVI",
        "Indu Mittapalli",
        "Pasupuleti Lakshmi Sai charan",
        "Prem sai",
        "Vayalapalli Yashwanth",
        "Praveen",
        "Raj kumar",
        "J.Hanveshith",
        "Vinay Kumar",
        "K Narasimha",
        "SIVAPURAM VENKATA SATYA HYNDAV",
        "Shreya"
    ]
}


#W, H = (1123, 794)


api = "https://api.npoint.io/0ac056978990354196e5"

PATH = "./cert.png"

# options = []
# for i in names.keys():
#     options.append(i)

font = ImageFont.truetype("Poppins-Medium.ttf", 100)
events = st.selectbox("Select Event name", events_data.keys())
name = st.selectbox(
    "Select your name for generating certificate", events_data[events])
name = name.title()
im = Image.open(PATH)
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
