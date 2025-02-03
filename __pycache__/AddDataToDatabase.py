import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendencerealtime-5faf2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "296":
        {"name": "Gourav Panigrahi",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year":"3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"


        },
    "419":
        {
            "name": "Rajkumar Mahapatra",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "R",
            "year":"3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "397":
        {
            "name": "Anurag Nahak",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "A",
            "year": "3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"

    },
    "301":
        {
            "name": "Satyanarayan  Jena",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "S",
            "year": "3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"
    },
    "433":
        {
            "name": "Suraj Kumar Dalai",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "X",
            "year": "3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"

    },
    "311":
        {
            "name": "A Shantilata Achasry",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "O",
            "year": "3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "67":
        {
            "name": "Mira Naik",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "M",
            "year": "3rd ",
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "275":
        {
            "name": "Subhalaxmi Pradhan",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "B",
            "year": "3rd ",
            "lTast_attendance_time": "2022-12-11 00:54:34"

        },
"002":
        {
            "name": "Nirmala Behera",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "B",
            "year": "2nd ",
            "lTast_attendance_time": "2022-12-11 00:54:34"
        },
"432":
        {
            "name": "S Tilak Prusty",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "B",
            "year": "2nd ",
            "Last_attendance_time": "2022-12-11 00:54:34"
        },

}

#for linking data to database
for key, value in data.items():
    ref.child(key).set(value)