import urllib
import facebook
import requests
import json

token = 'EAADDFenkkWMBAEG2Clr1UHIZATqkmMb6PZA5BKP1rejCJBrgUfYWXB63jAfXIyXDNWdqZBBxUO6gMuYISGOkw22g2zmE2yFUTPU2w3030x45FkisR6MSDyPiA5LdLLyLCxGenLb0fQXj1zD1LkZC2d9fI6odk94ZD'

graph = facebook.GraphAPI(access_token=token, version=2.7)


def get_all_pages(posts):
   allposts=[]
   allposts = posts['data']
   while(1):
      try:
         next_page_url=posts['paging']['next']  #get url for next page
      except KeyError:
         break
      posts = requests.get(next_page_url).json()
      allposts += posts['data']
   return allposts
   


def get_post_likes(post):
   mylikes=[]
   try:
     likes=graph.get_connections(post['id'],"likes")
     mylikes = get_all_pages(likes)
   except:
     pass 
   return mylikes


def get_liked_pages():
   mypages=[]
   pages = graph.get_connections('me',connection_name='likes')
   mypages = get_all_pages(pages)
   return mypages

def get_user_posts():
   myposts=[]

   #get my posts on page 1
   posts = graph.get_connections('me',connection_name='posts')
   #visit all pages
   myposts = get_all_pages(posts)
   H1 = []
   for n in range(150):
       row = []
       row.append(myposts[n]["id"])
       row.append(myposts[n]["created_time"])
       try:
          row.append(myposts[n]["message"])
       except KeyError:
          #row.append(myposts[n]["message"])
          row.append(" _Shared Story ")
       H1.append(row)
   for m in range(150):
       for n in range(3):
           print H1[m][n]
       print "\n"
       
   for m in range(150):
      post_ids = []
      post_ids = H1[m][0]
      post_created_time = []
      post_created_time = H1[m][1]
      post_message = []
      post_message = H1[m][2]
   
   return myposts


def get_user_details():
   #graph api does not allow to access all fields at once...so you have to list the fields you require!
   user = graph.get_object('me',fields='name,id,email,education,friends,age_range,birthday')
   name = graph.get_object('me',fields='name')
   id = graph.get_object('me',fields='id')
   name = name["name"]
   print "Name -" ,name
   id = id["id"]
   print "Id - ",id

   email = graph.get_object('me',fields='email')
   email = email["email"]
   print "Email - ",email

   '''
   I've not parsed this as this is none of my concern rn. :)
   #PARSE THIS!!
   education = graph.get_object('me',fields='education')
   education = education["education"]
   print "Education - ",education
   '''
   
   age_range = graph.get_object('me',fields='age_range')
   age_range_max = int(age_range["age_range"]["max"])
   age_range_min = int(age_range["age_range"]["min"])
   age_avg = (int(age_range["age_range"]["max"]) + int(age_range["age_range"]["min"]))/2
   print "Estimated Age - ",age_avg
   
   birthday = graph.get_object('me',fields='birthday')
   birthday = birthday["birthday"]
   print "Birthday - ",birthday

   about = graph.get_object('me',fields='about')
   about = about["about"]
   print "About - ",about

   #Check permission for this - 
   #address = graph.get_object('me',fields='address')
   #address = address["address"]
   #print "Address - ",address

   work = graph.get_object('me',fields='work')
   work_position = work["work"][0]["position"]["name"]
   work_location = work["work"][0]["location"]["name"]
   work_start_date = work["work"][0]["start_date"]
   work_employer = work["work"][0]["employer"]["name"]
   print "Work Details - \n"
   print "Work Place - ",work_employer
   print "Work Position - ",work_position
   print "Work StartDate - ",work_start_date
   print "Work Location - ",work_location
   
   #Check permission for this - 
   #relationship_status = graph.get_object('me',fields='relationship_status')
   #reltaionship_status = relationship_status["relationship_status"]
   #print "Relationship Status - ",relationsip_status

   tagged_places = graph.get_object('me',fields='tagged_places')
   tagged_data = tagged_places["tagged_places"]["data"]
   #Store the ids in an array and iterate using for loop
   
   H0 = []
   for n in range(10):
       row = []
       row.append(tagged_data[n]["id"])
       row.append(tagged_data[n]["created_time"])
       row.append(tagged_data[n]["place"]["name"])
       row.append(tagged_data[n]["place"]["location"]["latitude"])
       row.append(tagged_data[n]["place"]["location"]["longitude"])
       row.append(tagged_data[n]["place"]["location"]["city"])
       row.append(tagged_data[n]["place"]["location"]["zip"])
       row.append(tagged_data[n]["place"]["location"]["country"])
       H0.append(row)
   for m in range(10):
       for n in range(8):
           print H0[m][n]
       print "\n"
   for m in range(10):
      tagged_places_ids = []
      tagged_places_ids = H0[m][0]
      tagged_places_created_time = []
      tagged_places_created_time = H0[m][1]
      tagged_places_name = []
      tagged_places_name = H0[m][2]
      tagged_places_location = []
      tagged_places_location = str(H0[m][3])+ "," + str(H0[m][4])
      tagged_places_city = []
      tagged_places_city = H0[m][5]
      tagged_places_zip = []
      tagged_places_zip = H0[m][6]
      tagged_places_country = []
      tagged_places_country = H0[m][7]

   
   gender = graph.get_object('me',fields='gender')
   gender = gender["gender"]
   print "Gender - ",gender
   
   hometown = graph.get_object('me',fields='hometown')
   hometown = hometown["hometown"]["name"]
   print "Hometown - ",hometown
   
   location = graph.get_object('me',fields='location')
   location = location["location"]["name"]
   print "Location - ",location

   #saveFile = 
   return user

url = "https://graph.facebook.com/me?access_token=EAADDFenkkWMBAMBJgKl7ZBYPSP7AyIYG3iDcrOZAv5aq2sqNCmYaZCye5aaATaPPD65nK5dJzEL3aWIU2hv5EhS4y0FUpiKG5QNoL76keSjAgHfIoZAwtaeasWXQSkuwxiY5RLTShD68AFZCMCQjTZAn2ZAR26jxzTM3uduMYTPpFZBvYJmq0sI3peenCnuFfTsZD"

response = urllib.urlopen(url)
uid = json.loads(response.read())
print "User ID - ",uid

print "User Details - "
user_details = get_user_details()
print "User Posts(150 limit)"
user_posts_info = get_user_posts()
