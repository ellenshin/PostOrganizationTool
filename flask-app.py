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

subcategories = []
categories = []
post_types = [[][][][]]     #[0] = 'image,[1] = 'text',[2] = 'video', [3] = 'fb link',[4] = 'audio'
platforms = []
temppost = []


class Content():

    def __init__(self, list):
        self._initial_dict = {'platform': list[8], 'message': list[9], 'postID': list[0]}
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
        self._listofdict = []
        self._listofdict.append(self._initial_dict)

    def addPost(self, platform, message, post_id):
        tempdict = {'platform': platform, 'message': message, 'postID': post_id}
        self._listofdict.append(tempdict)
        return self._listofdict

def appenditem(obj):

    global post_types
    if obj._get_postType == 'image':
        post_types[0].append(obj)

    elif obj._get_postType =='text':
        post_types[1].append(obj)

    elif obj._get_postType == 'video':
        post_types[2].append(obj)

    elif obj._get_postType == 'fb link':
        post_types[3].append(obj)

    elif obj._get_postType == 'audio':
        post_types[4].append(obj)


def get_data():
    listofObj = []
    listofcid = []
    prev_obj = None

    with open('Large_Data_Set_Posts11.csv', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        contents = [row for row in reader]

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
        temp.append(campaignId)
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

        global temppost

        if gen_postType not in temppost:
            temppost.append(gen_postType)

        global subcatagories

        if sub_category not in subcategories:
            subcategories.append(sub_category)

        if prev_obj == None:
            obj = Content(temp)
            prev_obj = obj
            listofcid.append(campaignId)
            listofObj.append(obj)
        elif prev_obj._campaignID == campaignId:
            prev_obj.addPost(platform, message, post_id)
        else:
            obj = Content(temp)
            listofcid.append(campaignId)
            prev_obj = obj
            listofObj.append(prev_obj)
    print(temppost)
    listofObj.append(prev_obj)
    print(len(listofObj))

    return listofObj


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