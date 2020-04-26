from InstagramAPI import InstagramAPI



users_list = []
following_users = []
follower_users = []

api = InstagramAPI("01096458519","skek8641!@#")
api.login()
api.getTotalSelfFollowers()
result = api.LastJson
for user in result['users']:
    follower_users.append(user['username'])
api.getSelfUserFollowers()
result = api.LastJson
for user in result['users']:
    follower_users.append(user['username'])
print(follower_users)


'''non_check_list=[]
all_follower ="jiheu__n2 hyeonwoo_shin flylikehawk ooooong_93 bbyhobby jhjhphoto orinalda1 sweetandsourchickenho u_jit_su sohee.da__ iamhunbae 90frosh_1 kokonutreee ikujinnim woni2y vvhyunjungvv hyuuuuuuunnnnnnn chinaplane zuzu_zzing 2020_connection stitch9403 c.haerin mabe_onlyfire min__dora jin__mung eumdong_zzang ssam_mu_27 yesjiyoung pixooture hienem_2 taewonjin 00___00_s haejji_ jungsae.a gelin_jji hyeseon_oct15 jun___.___ho jeju_birdboy jejucafe_birdboy y_jenn_ hyojune1999 hxrf2016 idontthinksoeun eres_snap cyooonjung changwooson kkungs_s oppshyun p.__.sam liht_woon_ zi.eunn yeonzoo__ 9honey_ uju.bak.7 howoorock hyeonghoonk index.park loml1105 ziyoeng_e a__kzxz jiwony_m su9yeon zinc.world jungah_127 j_huiyeol hy_wellcomm keonwoo_aid moong825 yerimirim tmdwls0830 julia_08ss choi._.sky kawori9570 e_grande_b madbee_p yoon_i112 idealtype0410 jinsu2873 venus_sg __hb.b bhyun2 jeong.yeonghyeok dlswo healthcenter_hanyang ymie9999 kkpd hyuun._.vely young.kim61 o_joonseok pu_rumm im_ty0421 minjun7682 e.huiz_z heungminjinjin ijihye__ dkdlsdn jaehyun2633 in_cook_eat 98_hyogui choi_rish_er s_ung_s_ung hochankeem 9190._.y _jay_star17 iseeun4 coejaeil7684 jmshin11 eunji_eunoia yuhyeongtyag cookiecooky_chan p3achj3lly sangmu639 ddu_u__ddu___ shoes_archive hyen.i__ baebae0519 sayless._.domore say_jjung minggg.42 happy_rain0521 meaningful_______ birth_on_march juhee__cha go_mj0421 um_zzung songs_1222 ag_almeori hellomynameisjinhyeok centerpark42 yootaj jayssion kim__minwoo 674qgorbsgs kqcss143 10.09_95 jin.__.nij 2asyy_h ykh5293 dhdhdh9977 yeah_rang_ aaa.b0ut_sy kim.jo_o yootajjjj urbram_ mm_minaa__ p.sss.j hyunejoon pyousung jungduckin8765 x_sum_in wlsdlstodrkr jwwwk_ saea_izz jun.5_ ssaeah__ gnsworla min_chelin miiiin_y honey.picture hannahannah______ eu.nseo seung__hyuk buzzy___z jwsong0617 don9hyun_ soon_hyeons spring_uni1110 yuestev baykop_panasonic noji.94 muchhappything 5rongx.x oo_647 mudong1118 olddonkey0 g_won_188 heeknows bb.bppppp sinnnn_95 taco_kim_ dydhem3 geniessu feverk3144 ch_hyunjong 2ternal_flame sungbin940611 dawon_ny don6hui outstanding_base yewon_toon chaeng_.i sungancho951025 00ye0n young._s_ j_yooniverse soo_hyuk22 ha5hin goseok.geul easywoon9 satanghoon_ hayounng2 chambut_kim taeklim.kim ig_jayee hansssseul wonbbinnn seounn_a guilherme_ys kahyony hyuns2un 24yerika sojeongsgift chocmh suki__is ppink_un chaji1105 yura_or_caroline miinnnng lopyjjin"
all_follower = all_follower.split()

for i in follower_users:
    if i not in all_follower:
        non_check_list.append(i)
print(non_check_list)'''