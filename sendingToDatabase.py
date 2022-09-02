import requests
import datetime

def timeStamp():
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S")
    return  timestampStr



API_ENDPOINT = "http://10.16.89.62/meteraninfo/api_post.php"

reading_value = 100000
created_at = timeStamp()
prediction_score = 95.8
status = "normal"

test_files = {
    "reading_value"     : reading_value,
    "created_at"        : created_at,
    "prediction_score"  : prediction_score,
    "status"            : status,
    "img"               : open("research/itron_meteran.jpg", "rb")

}

test_response = requests.post(API_ENDPOINT, files = test_files)
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")

