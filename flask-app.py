from os import chdir
from os.path import dirname
import csv


from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# DEMO STUFF

@app.route('/')
def view_hello():
    return 'Hello World!'

"""
@app.route('/demo-1/')
def view_demo_1():
    return render_template('demo-1.html', name='Justin')

@app.route('/demo-2/<name>/')
def view_demo_2(name):
    return render_template('demo-1.html', name=name)

@app.route('/demo-3/')
def view_demo_3():
    names = ['Alice', 'Bob', 'Charlie']
    return render_template('demo-3.html', salutation='Roll call', names=names)
"""


class Content():

    def __init__(self, list):
        self._post_id = list[0]
        self._handle = list[1]
        self._postDate = list[2]
        self._postType = list[3]
        self._gen_postType = list[4]
        self._twitter_comment = list[5]
        self._twitter_retweet = list[6]
        self._postUrl = list[7]
        self._platform = list[8]
        self._message = list[9]
        self._cta_prediction = list[10]
        self._relevant_prediction = list[11]
        self._comments = list[12]
        self._shares = list[13]
        self._likes = list[14]
        self._views = list[15]
        self._campaignID = list[16]
        self._campaign_name = list[17]
        self._campaign_startDate = list[18]
        self._campaign_endDate = list[19]
        self._project_goal = list[20]
        self._project_currency = list[21]
        self._project_staffPick = list[22]
        self._sub_category = list[23]
        self._project_url = list[24]
        self._project_pledgeAmount = list[25]
        self._project_backerCount = list[26]
        self._succeeded = list[27]
        self._prediction = list[28]
        self._sell_relevant = list[29]
        self._listofposts = []

        tempdict = {
        "post_id" : self._post_id,
        "handle" : self._handle,
        "postDate" : self._postDate,
        "postType" : self._postType,
        "gen_postType" : self._gen_postType,
        "twitter_comment" : self._twitter_comment,
        "twitter_retweet" : self._twitter_retweet,
        "postUrl" : self._postUrl,
        "platform" : self._platform,
        "message" : self._message,
        "cta_prediction" : self._cta_prediction,
        "relevant_prediction" : self._relevant_prediction,
        "comments" : self._comments,
        "shares" : self._shares,
        "likes" : self._likes,
        "views" : self._views,
        'CampaignId' : self._campaignID,
        'campaign_name' : self._campaign_name,
        'campaign_startDate' : self._campaign_startDate,
        'campaign_endDate' : self._campaign_endDate,
        'project_goal' : self._project_goal,
        'project_currency' : self._project_currency,
        'project_staffPick' : self._project_staffPick,
        'sub_category' : self._sub_category,
        "project_url" : self._project_url,
        'project_pledgeAmount' : self._project_pledgeAmount,
        'project_backerCount' : self._project_backerCount,
        'succeeded' : self._succeeded,
        'prediction' : self._prediction,
        'sell_relevant' : self._sell_relevant
        }
        self._listofposts.append(tempdict)


    def __repr__(self):
        return '|' + self._gen_postType + '|'

    def addPost(self, cells):
        temp = []

        post_id = cells[1]
        handle = cells[2]
        postDate = cells[3]
        postType = cells[4]
        gen_postType = cells[5]
        twitter_comment = cells[6]
        twitter_retweet = cells[7]
        postUrl = cells[8]
        platform = cells[9]
        message = cells[10]
        cta_prediction = cells[11]
        relevant_prediction = cells[12]
        comments = cells[13]
        shares = cells[14]
        likes = cells[15]
        views = cells[16]
        campaignId = cells[17]
        campaign_name = cells[18]
        campaign_startDate = cells[19]
        campaign_endDate = cells[20]
        project_goal = cells[21]
        project_currency = cells[22]
        project_staffPick = cells[23]
        sub_category = cells[24]
        project_url = cells[25]
        project_pledgeAmount = cells[26]
        project_backerCount = cells[27]
        succeeded = cells[28]
        prediction = cells[29]
        sell_relevant = cells[30]

        tempdict = {
            "post_id": post_id,
            "handle": handle,
            "postDate": postDate,
            "postType": postType,
            "gen_postType": gen_postType,
            "twitter_comment": twitter_comment,
            "twitter_retweet": twitter_retweet,
            "postUrl": postUrl,
            "platform": platform,
            "message": message,
            "cta_prediction": cta_prediction,
            "relevant_prediction": relevant_prediction,
            "comments": comments,
            "shares": shares,
            "likes": likes,
            "views": views,
            'CampaignId': campaignId,
            'campaign_name': campaign_name,
            'campaign_startDate': campaign_startDate,
            'campaign_endDate': campaign_endDate,
            'project_goal': project_goal,
            'project_currency': project_currency,
            'project_staffPick': project_staffPick,
            'sub_category': sub_category,
            "project_url": project_url,
            'project_pledgeAmount': project_pledgeAmount,
            'project_backerCount': project_backerCount,
            'succeeded': succeeded,
            'prediction': prediction,
            'sell_relevant': sell_relevant
        }

        self._listofposts.append(tempdict)
        return self._listofposts

subcategories = []
categories = []

glpost_types = []     #[0] = 'image,[1] = 'text',[2] = 'video', [3] = 'fb link',[4] = 'audio'
glimage_types = []
gltext_types = []
glvideo_types = []
gllink_types = []
glaudio_types = []
glpost_types.append(glimage_types)
glpost_types.append(gltext_types)
glpost_types.append(glvideo_types)
glpost_types.append(gllink_types)
glpost_types.append(glaudio_types)


def addItem(obj):

    global glpost_types
    global glimage_types
    global gltext_types
    global glvideo_types
    global gllink_types
    global glaudio_types

    for dict in obj._listofposts:

        if dict['gen_postType'] == "image": glimage_types.append(dict)

        if dict['gen_postType'] == "text" : gltext_types.append(dict)

        if dict['gen_postType'] == "video" : glvideo_types.append(dict)

        if dict['gen_postType'] == "fb link" : gllink_types.append(dict)

        if dict['gen_postType'] == "audio" : glaudio_types.append(dict)


def get_data():
    listofObj = []
    listofcid = []
    prev_obj = None
    global subcatagories
    global platforms

    with open('Large_Data_Set_Posts11.csv', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        contents = [row for row in reader]

    running = True
    while(running):
        for row in contents[1:]:
            temp = []
            cells = row
            post_id = cells[1]
            handle = cells[2]
            postDate = cells[3]
            postType = cells[4]
            gen_postType = cells[5]
            twitter_comment = cells[6]
            twitter_retweet = cells[7]
            postUrl = cells[8]
            platform = cells[9]
            message = cells[10]
            cta_prediction = cells[11]
            relevant_prediction = cells[12]
            comments = cells[13]
            shares = cells[14]
            likes = cells[15]
            views = cells[16]
            campaignId = cells[17]
            campaign_name = cells[18]
            campaign_startDate = cells[19]
            campaign_endDate = cells[20]
            project_goal = cells[21]
            project_currency = cells[22]
            project_staffPick = cells[23]
            sub_category = cells[24]
            project_url = cells[25]
            project_pledgeAmount = cells[26]
            project_backerCount = cells[27]
            succeeded = cells[28]
            prediction = cells[29]
            sell_relevant = cells[30]

            temp.append(campaignId)
            temp.append(post_id)
            temp.append(handle)
            temp.append(postDate)
            temp.append(postType)
            temp.append(gen_postType)
            temp.append(twitter_comment)
            temp.append(twitter_retweet)
            temp.append(postUrl)
            temp.append(platform)
            temp.append(message)
            temp.append(cta_prediction)
            temp.append(relevant_prediction)
            temp.append(comments)
            temp.append(shares)
            temp.append(likes)
            temp.append(views)
            temp.append(campaign_name)
            temp.append(campaign_startDate)
            temp.append(campaign_endDate)
            temp.append(project_goal)
            temp.append(project_currency)
            temp.append(project_staffPick)
            temp.append(sub_category)
            temp.append(project_url)
            temp.append(project_pledgeAmount)
            temp.append(project_backerCount)
            temp.append(succeeded)
            temp.append(prediction)
            temp.append(sell_relevant)

            if prev_obj == None:
                obj = Content(temp)
                prev_obj = obj
                listofcid.append(campaignId)
                listofObj.append(obj)
            elif prev_obj._campaignID == campaignId:
                prev_obj.addPost(temp)
            else:
                obj = Content(temp)
                listofcid.append(campaignId)
                listofObj.append(obj)
                prev_obj = obj

            if sub_category not in subcategories:
                subcategories.append(sub_category)

        running = False

    for object in listofObj:
        addItem(object)

    print('-------')
    print('-------')

    #print(len(post_types[3]))
    #print(len(post_types[4]))



@app.route('/directory/')
def view_directory():
    return 'FIXME'

@app.route('/directory/<username>/')
def view_student(username):
    return 'FIXME'

# DON'T TOUCH THE CODE BELOW THIS LINE

@app.route('/css/<file>')
def view_css(file):
    return send_from_directory('css', file)

if __name__ == '__main__':
    #chdir(dirname(__file__))
    get_data()
    #app.run(debug=True)