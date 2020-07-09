from rest_framework.response import Response
from rest_framework.decorators import api_view

month = {"Jan": 0, "Feb": 31, "Mar": 59, "Apr": 90,
"May": 120, "Jun": 151, "Jul": 181, "Aug": 212,
"Sep": 243, "Oct": 273, "Nov": 304, "Dec": 334}

## Convert the date in 365 days for easly comparing  
def convertInDays(dates): 
    dates = dates.split(" ")
    monthVal = month[dates[1].strip().title()]
    datesVal = monthVal+int(dates[0])
    return datesVal
## Function for findig the maximum disjoint intervals 
## Greedy approaches has been used to solve the problem

@api_view(['POST','GET'])
def getMaxMovie(request):
    if request.method == 'POST':
        movie_list = request.data["movie_list"]
        movieInNum = []
        final_list=[]
        for key,val in movie_list.items():
            movieid =  int(key)  
            movie_start_date = convertInDays(val["start_date"])
            movie_end_date = convertInDays(val["end_date"])
            movieInNum.append([movieid,movie_start_date,movie_end_date])
        movieInNum.sort(key = lambda x: x[2])
        final_list.append(movieInNum[0])
        last_work_day = movieInNum[0][2]
        for i in range (1,len(movieInNum)):
            next_work_day = movieInNum[i][1]
            next_last_day = movieInNum[i][2]
            if next_work_day > last_work_day:
                final_list.append(movieInNum[i])
                last_work_day=next_last_day
        movie_json={"movie_list":{}}
        for i in final_list:
            movie_json["movie_list"][str(i[0])] = movie_list[str(i[0])]
    elif request.method == 'GET':
        movie_json = {"movie_list":
                    {
                "1":{
                    "movie":"*Name of movie*",
                    "start_date":"*date Month(Jan, Feb, etc*)",
                    "end_date":"*date Month(Jan, Feb, etc*)"
                    },
                "2":{
                    "movie":"Rock",
                    "start_date":"20 Jan",
                    "end_date":"30 Jan"
                    }
                }
            }
    return Response(movie_json)