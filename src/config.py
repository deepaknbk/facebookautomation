
# https://www.facebook.com/groups/2512957342342147 - Dev Test
# https://www.facebook.com/groups/473152883710976 - Test2
# https://www.facebook.com/groups/751322535510799 - Test4
# https://www.facebook.com/padati.jewels - Padati Jewelsd

image_path="C:/Users/User/PycharmProjects/facebookautomation/images/"

FB_group_props= {

'DevTest': {
        'url':"https://www.facebook.com/groups/2512957342342147",
        'wall_post_xpath':"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span",
        'popup_post_xpath':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div",
        'post_img_flag':True,
        'upload_img_input_xpath':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input",
        'submit_post':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div"
    },
'Test2': {
        'url':"https://www.facebook.com/groups/473152883710976",
        'wall_post_xpath':"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span",
        'popup_post_xpath':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div",
        'post_img_flag':True,
        'upload_img_input_xpath':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input",
        'submit_post':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div"

    },

'PadatiJewels': {
        'url':"https://www.facebook.com/padati.jewels",
        'wall_post_xpath':"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span",
        'popup_post_xpath':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div",
        'post_img_flag':False,
        'upload_img_input_xpath':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/input",
        'submit_post':"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div"
    }


}