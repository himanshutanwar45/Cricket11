import pyodbc
import os
import requests
import json
from Classes.Connection.Connection import Connection
from dotenv import load_dotenv


class APITeamModules:

    load_dotenv()

    ################################ Get Team List ##############################################################

    def APIGetTeamList(user_code):
        conn = pyodbc.connect(Connection.GetConnectionString())

        team_type_list = ['international','league','domestic','women']

        response_list = []

        for rows in team_type_list:
            url = f"https://cricbuzz-cricket.p.rapidapi.com/teams/v1/{rows}"

            headers = {
                "X-RapidAPI-Key": os.getenv("API_KEY"),
                "X-RapidAPI-Host": os.getenv("API_HOST")
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                teams_data = response.json()

                for team in teams_data['list']:
                    team['teamType'] = rows

            response_list.append(teams_data['list'])

        with open('TeamList.json', 'w') as file:
            json_data = json.dump(response_list, file, indent=4)

        json_string = json.dumps(response_list)

        cursor = conn.cursor()
        cursor.execute("EXEC Sp_Add_Team_Data ?,?",
                    (json_string, user_code))
        data = cursor.fetchall()
        data_list = []
        conn.commit()
        for rows in data:
            data_dict = {
                'Error_Code': rows[0],
                'Error_Name': rows[1]
            }
            data_list.append(data_dict)
        conn.close()
        return data_list

        # response = {
        #     "list": [
        #         {
        #             "teamName": "Test Teams"
        #         },
        #         {
        #             "teamId": 2,
        #             "teamName": "India",
        #             "teamSName": "IND",
        #             "imageId": 172115,
        #             "countryName": "India"
        #         },
        #         {
        #             "teamId": 96,
        #             "teamName": "Afghanistan",
        #             "teamSName": "AFG",
        #             "imageId": 172188
        #         },
        #         {
        #             "teamId": 27,
        #             "teamName": "Ireland",
        #             "teamSName": "IRE",
        #             "imageId": 172141
        #         },
        #         {
        #             "teamId": 3,
        #             "teamName": "Pakistan",
        #             "teamSName": "PAK",
        #             "imageId": 172116
        #         },
        #         {
        #             "teamId": 4,
        #             "teamName": "Australia",
        #             "teamSName": "AUS",
        #             "imageId": 172117
        #         }

        #     ],
        #     "status_code": "200"

        # }
        # return response
        # with open('TeamList.json', 'w') as file:
        #     json_data = json.dump(response, file, indent=4)
        # json_string = json.dumps(response)
        # conn = pyodbc.connect(Connection.GetConnectionString())
        # cursor = conn.cursor()
        # cursor.execute("EXEC Sp_Add_Team_Data ?,?", (json_string, user_code))
        # data = cursor.fetchall()
        # conn.commit()
        # data_list = []
        # for rows in data:
        #     data_dict = {
        #         'Error_Code': rows[0],
        #         'Error_Name': rows[1]
        #     }
        #     data_list.append(data_dict)
        # conn.close()
        # return data_list

    ##################       END           ###################################

    ################################ Get Team Player By Team Id##############################################################
    def APIGetPlayerByTeamId(user_code, team_id):
        conn = pyodbc.connect(Connection.GetConnectionString())
        url = f"https://cricbuzz-cricket.p.rapidapi.com/teams/v1/{team_id}/players"

        headers = {
            "X-RapidAPI-Key": os.getenv("API_KEY"),
            "X-RapidAPI-Host": os.getenv("API_HOST")
        }

        response = requests.get(url, headers=headers)

        cricket_team = response.json()
        current_category = None
        for player in cricket_team['player']:
            if player['name'] == 'BATSMEN':
                current_category = 'BATSMEN'
            elif player['name'] == 'ALL ROUNDER':
                current_category = 'ALL ROUNDER'
            elif player['name'] == 'WICKET KEEPER':
                current_category = 'WICKET KEEPER'
            elif player['name'] == 'BOWLER':
                current_category = 'BOWLER'
            else:
                player['category'] = current_category

            player['teamId'] = team_id

        if response.status_code == 200:
            with open('TeamList.json', 'w') as file:
                json_data = json.dump(cricket_team, file, indent=4)

            json_string = json.dumps(cricket_team)
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_Add_Player_Data ?,?,?",
                           (json_string, team_id, user_code))
            data = cursor.fetchall()
            data_list = []
            conn.commit()
            for rows in data:
                data_dict = {
                    'Error_Code': rows[0],
                    'Error_Name': rows[1]
                }
                data_list.append(data_dict)
            conn.close()
            return data_list

        else:
            data_list = []
            data_dict = {
                'Error_Code': response.status_code,
                'Error_Name': 'Error while calling api'
            }
            data_list.append(data_dict)
            conn.close()
            return data_list

        # response = {
        #     "player": [
        #         {
        #             "name": "BATSMEN",
        #             "imageId": 174146
        #         },
        #         {
        #             "id": "10863",
        #             "name": "Fakhar Zaman",
        #             "imageId": 352419,
        #             "battingStyle": "Left-hand bat",
        #             "bowlingStyle": "Left-arm orthodox"
        #         },
        #         {
        #             "id": "8364",
        #             "name": "Imam-ul-Haq",
        #             "imageId": 352420,
        #             "battingStyle": "Left-hand bat"
        #         },
        #         {
        #             "id": "8359",
        #             "name": "Babar Azam",
        #             "imageId": 352417,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm offbreak"
        #         },
        #         {
        #             "id": "9565",
        #             "name": "Asif Ali",
        #             "imageId": 244935,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm medium"
        #         },
        #         {
        #             "name": "ALL ROUNDER",
        #             "imageId": 174146
        #         },
        #         {
        #             "id": "8299",
        #             "name": "Haris Sohail",
        #             "imageId": 170777,
        #             "battingStyle": "Left-hand bat",
        #             "bowlingStyle": "Left-arm orthodox"
        #         },
        #         {
        #             "id": "360",
        #             "name": "Mohammad Hafeez",
        #             "imageId": 170776,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm offbreak"
        #         },
        #         {
        #             "id": "33",
        #             "name": "Shoaib Malik",
        #             "imageId": 170775,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm offbreak"
        #         },
        #         {
        #             "id": "11186",
        #             "name": "Shadab Khan",
        #             "imageId": 352424,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm legbreak"
        #         },
        #         {
        #             "id": "10408",
        #             "name": "Imad Wasim",
        #             "imageId": 170782,
        #             "battingStyle": "Left-hand bat",
        #             "bowlingStyle": "Left-arm orthodox"
        #         },
        #         {
        #             "name": "WICKET KEEPER",
        #             "imageId": 174146
        #         },
        #         {
        #             "id": "881",
        #             "name": "Sarfaraz Ahmed",
        #             "imageId": 170787,
        #             "battingStyle": "Right-hand bat"
        #         },
        #         {
        #             "name": "BOWLER",
        #             "imageId": 174146
        #         },
        #         {
        #             "id": "1051",
        #             "name": "Wahab Riaz",
        #             "imageId": 170809,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Left-arm fast"
        #         },
        #         {
        #             "id": "12160",
        #             "name": "Shaheen Afridi",
        #             "imageId": 352430,
        #             "battingStyle": "Left-hand bat",
        #             "bowlingStyle": "Left-arm fast-medium"
        #         },
        #         {
        #             "id": "11320",
        #             "name": "Hasan Ali",
        #             "imageId": 352428,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm fast-medium"
        #         },
        #         {
        #             "id": "14248",
        #             "name": "Mohammad Hasnain",
        #             "imageId": 244952,
        #             "battingStyle": "Right-hand bat",
        #             "bowlingStyle": "Right-arm fast-medium"
        #         },
        #         {
        #             "id": "1917",
        #             "name": "Mohammad Amir",
        #             "imageId": 170813,
        #             "battingStyle": "Left-hand bat",
        #             "bowlingStyle": "Left-arm fast-medium"
        #         }
        #     ]
        # }

        # cricket_team = response
        # current_category = None
        # for player in cricket_team['player']:
        #     if player['name'] == 'BATSMEN':
        #         current_category = 'BATSMEN'
        #     elif player['name'] == 'ALL ROUNDER':
        #         current_category = 'ALL ROUNDER'
        #     elif player['name'] == 'WICKET KEEPER':
        #         current_category = 'WICKET KEEPER'
        #     elif player['name'] == 'BOWLER':
        #         current_category = 'BOWLER'
        #     else:
        #         player['category'] = current_category

        #     player['teamId'] = team_id

        # with open('TeamList.json', 'w') as file:
        #     json_data = json.dump(cricket_team, file, indent=4)
        # json_string = json.dumps(cricket_team)

        # conn = pyodbc.connect(Connection.GetConnectionString())
        # cursor = conn.cursor()

        # cursor.execute("EXEC Sp_Add_Player_Data ?,?,?",(json_string,team_id, user_code ))
        # data = cursor.fetchall()
        # conn.commit()
        # data_list = []
        # for rows in data:
        #     data_dict = {
        #         'Error_Code': rows[0],
        #         'Error_Name': rows[1]
        #     }
        #     data_list.append(data_dict)
        # conn.close()
        # return data_list

    ################               END      ################################

    ################################ Get Team Player info By Player Id#########################################################

    def APIGetPlayerInfoByPlayerId(user_code, player_id):
        conn = pyodbc.connect(Connection.GetConnectionString())
        url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}"

        headers = {
            "X-RapidAPI-Key": os.getenv("API_KEY"),
            "X-RapidAPI-Host": os.getenv("API_HOST")
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open('TeamList.json','w') as file:
                json_data = json.dump(response.json(),file,indent=4)

            json_string = json.dumps(response.json())
            cursor = conn.cursor()
            cursor.execute("EXEC Sp_Add_Player_Info ?,?,?",(json_string,player_id,user_code))
            data = cursor.fetchall()
            data_list = []
            conn.commit()
            for rows in data:
                data_dict = {
                    'Error_Code':rows[0],
                    'Error_Name':rows[1]
                }
                data_list.append(data_dict)
            conn.close()
            return data_list

        else:
            data_list=[]
            data_dict = {
                'Error_Code':response.status_code,
                'Error_Name':'Error while calling api'
            }
            data_list.append(data_dict)
            conn.close()
            return data_list

        # response = {
        #     "id": "1413",
        #     "bat": "Right Handed Bat",
        #     "bowl": "Right-arm medium",
        #     "name": "Virat Kohli",
        #     "nickName": "Kohli",
        #     "height": "5 ft 9 in (175 cm) ",
        #     "role": "Batsman",
        #     "birthPlace": "Delhi",
        #     "intlTeam": "India",
        #     "teams": "India, Delhi, India Red, India U19, Royal Challengers Bangalore, Board Presidents XI, North Zone, Indians, India A, Asia XI",
        #     "DoB": "November 05, 1988 (35 years)",
        #     "image": "http://i.cricketcb.com/stats/img/faceImages/1413.jpg",
        #     "bio": "A spunky, chubby teenager with gelled hair shot to fame after leading India to glory in the Under-19 World Cup at Kuala Lumpur in early 2008. In an Indian team filled with saint-like icons worthy of their own hagiographies, Virat Kohli, with his most un-Indian, bad-boy intensity, would clearly be an outcast.  <br/><br/> <b>Grind through the ranks</b> <br/><br/> He soon joined the senior Men in Blue in Sri Lanka, come August 2008. In the absence of the regular openers, Virat Kohli was given a chance to open the batting in the ODI series. He played some commendable knocks in his extended run as an opener, as India went on to win the ODI series. However, the established and formidable pair of Tendulkar and Sehwag kept Kohli out of the team  <br/><br/> The 20-year-old continued to impress for Delhi and dominated attacks, clearly demonstrating that he belonged at a much higher level; that junior cricket was beneath his standards. Kohli then traveled to Australia in 2009 for the Emerging players tournament and stamped his authority all over the Bowling_Style attacks. He added big-match temperament to his r\u00e9sum\u00e9 too, lacing a fluent hundred in the final against South Africa, and guiding his team to a clinical victory. The young prodigy, barely old enough to receive his man-of-the-match champagne, ended the tournament with 398 runs from 7 outings with two centuries and two fifties, ensuring that he remained fresh in the selectors minds.  <br/><br/> <b>Cementing a national spot</b> <br/><br/> The selectors had no choice but to give Kohli another go in the Indian side, and this time he strung together a number of impressive scores. After being given an extended run, he repaid their faith by notching up his maiden ODI hundred in an impressive run-chase against Sri Lanka in December 2009 - his first of many exemplary knocks in run-chases. In the World Cup final of 2011, the biggest stage of them all, Kohli, along with his Delhi teammate Gautam Gambhir, pulled off a largely underrated rescue effort with an 83-run stand after losing the openers early. This knock played a crucial role in setting the platform for MS Dhonis fabled knock of 91*, which eventually won India the World Cup on that enchanting evening in Mumbai.  <br/><br/> In the hangover of the World Cup euphoria, Kohli continued to take giant strides in the limited-overs format. Three years after his ODI debut, he was finally handed the coveted Test cap in the Caribbean islands in July 2011, owing to the need to rest the senior players. After a series each against the Dukes ball and the SG ball, it was now time for his trial against the Kookaburra Down Under. In the first two Tests, he seemed to lack the technique to play in Australia, maintaining his low stance on the bouncy tracks. He also had a rather restricting trigger movement with his front-foot routinely coming across towards off-stump, thereby hindering the necessary movement to play back-foot shots such as the pull and the cut.  <br/><br/> <b>A baptism by fire Down Under</b> <br/><br/> The selectors and the captain persisted with him going into the 3rd Test, and he delivered a break-through performance on a bouncy Perth wicket - an impressive 75 - where a visible change in technique was visible. He managed to stand tall, with a more open stance, and exhibited the back-foot shots in his repertoire during the course of the innings. The volatile Kohli managed to overshadow his impropriety in conduct with his performance in the final Test of the series. Notching up Indias only century of a disastrous tour, Kohli was the shining light in amidst the chaos, as he stroked his way to a hundred in Adelaide exhibiting the will to improve and extraordinary focus under pressure in the searing heat and pressure of Australia. <br/><br/> While he grappled and clawed his way into the Test side, he went on a record-breaking spree in ODIs: the Indian record for the fastest to multiples-of-thousand runs in ODIs, culminating in the world record for the fastest to 9000 runs in ODIs. He was also the highest run-scorer for India in ODIs for three consecutive calendar years - 2010, 2011 and 2012 and won the ICC ODI cricketer of the year award in 2012.  <br/><br/> <b>That break-through innings\u2026</b> <br/><br/> We remember the accolades, but where did it all begin? Theres always the one innings that made the world sit up and take notice; the 86-ball knock which he started off as a brash boy, but ended as a man. Chasing an improbable target of 321 off 40 overs to stay alive in the tournament, he laid into the Sri Lankan bowlers and carted his way to 133*, getting India home with more than 2 overs to spare, practically pulling them out of the airport after M.S. Dhoni rather ignorantly remarked that India had already been eliminated from the tournament.  <br/><br/> King Kohli had arrived. The king of the run-chase, and a plethora of ODI records in the modern age. <br/><br/> <b>Batting technique and idiosyncrasies</b> <br/><br/> Kohli has a seemingly hot head on his shoulders, but he channels all his anger while he is batting. Known to be an aggressive batsman always on the lookout for runs, he has a fairly sound , albeit slightly unconventional technique, which makes him judge the length of the ball earlier than most, and amazingly quick wrists to run his hands through the ball, even against fast bowlers. He is equally adept against pace and spin, and never looks ungainly at the crease. With nimble foot-movement against the spinners, he is known to be quite destructive when the situation demands it. He has had to fill some rather big shoes of his predecessors, and has done an admirable job to say the least.  <br/><br/> <b>Captaincy and a change in technique</b> <br/><br/> With regular captain MS Dhoni ailing from an injury, Kohli was named stand-in captain for the first Test at Adelaide. After an abysmal tour of England, critics were sceptical of Kohlis performance in Australia in the Border-Gavaskar trophy in December. Kohli proved that they couldnt have been more wrong, as he scored two fluent hundreds in the first Test at Adelaide. His second innings masterclass of 141 almost pulled off a stunning run-chase on a notorious 5th day rank-turner, and went on to score a total of four hundreds on this tour. Saying that he had silenced critics would be an understatement. <br/><br/> As India prepared for their title defence ahead of the 2015 World Cup Down Under, with the catch phrase Wont give it back doing the rounds, Virat Kohli was touted to be a key performer for India. The Indians had a terrible run in Australia, having failed to win a single match in the Test series as well as the succeeding ODI tri-series. Kohli started off in signature fashion, with a typically stroke-filled hundred against Pakistan as India maintained their unbeaten run against their arch-rivals in ICC events. As India stormed into the semi-finals unbeaten, Kohlis form continued to take an uncharacteristic dip, culminating in a painstaking 1 in the semi-final loss against the co-hosts and eventual champions, Australia.  <br/><br/> Kohli, the then full-time Test captain, toured Sri Lanka with a young side without the services of Mahendra Singh Dhoni, wary of the Sri Lankan spinners fabled 4th innings con-job. After losing the first Test, Kohlis India recorded a dramatic come-from-behind win in the series, going on to win 2-1. Kohli continued to build on his auspicious start to Test captaincy as he led them to a rout of the South Africans on a series of rank-turners all around India. He had a quiet series with the bat, as the more stoic batsmen of his team took over. Nonetheless, the triumph took India to the No. 1 spot in the ICC Test rankings for the first time since they forfeited it to England after the forgettable white-wash in 2011.  <br/><br/> He continued his emphatic run in T20 cricket (and running) like a man possessed though, thrashing boundaries with ridiculous ease. Despite an 89* in the 2016  semi-final against the West Indies (extending his inhuman run of form in the format), Indias Bowling_Style panicked at a crucial stage. One had to feel sorry for him as he had to make do with the Player of the tournament award for the second successive Twenty20 World Cup; a distinction he wouldve gladly exchanged for the elusive World T20 trophy. Kohlis thirst for runs showed no signs of slowing down as he looted a small matter of 973 runs during the 2016 edition of the Indian Premier League, the most (by far) by any batsman in the history of the tournament - as he led his Royal Challengers Bangalore (RCB) franchise to a runners-up finish.  <br/><br/> However, it isnt beyond Kohli to prove his critics wrong yet again, as he continues to take criticism on his stride, setting new standards for modern batsmanship. And as a captain, he had his ups and downs, marred with a bit of controversy towards the end of his tenure. Kohli also became the first Indian, as well as the first Asian captain, to return victorious from Down Under when India won the 4-match Test series 2-1 (2018-19). Under Kohli, India also emerged as the number one Test side for five successive years (2016-2021). <br/><br/> <b>The final frontier</b> <br/><br/> In the first week of 2018, Kohli went on to lead India in South Africa, a few weeks after he tied the knot with Indian actress and long-time girlfriend, Anushka Sharma. India went on to concede the series in the first two Tests, but came back to win the third Test match on a difficult wicket. In a series full of difficult wickets, Kohli exhibited tighter technique than he had in England, and batted better than he did in his more prolific tour of South Africa in 2013/14. Kohli went on to conquer his (personal) final frontier in England later in 2018 too, scoring 593 runs in 10 innings, including 2 hundreds, and not conceding his wicket to his fabled nemesis, Anderson, even once. India went on to lose the series 1-4, and Kohlis record as captain was tainted by two consecutive Test series losses away.  <br/><br/> Nevertheless, on a personal level, he had left no stone unturned to transform himself into the most consistent and versatile batsman of his age, and arguably the better of the Big Four. In October 2018, during the second of 3 consecutive hundreds against the West Indies in ODIs, he went on to become the fastest batsmen to reach the 10,000-run mark in ODIs, trouncing Sachin Tendulkar by a staggering 54 innings. Despite arguments about the two new balls, better bats, batting-friendly conditions, and more lethal bowlers, it was difficult to deny that this was a statistical outlier, very much along the lines of 99.94 - perhaps unlikely to ever be trounced.   <br/><br/> However, being a cricket romantic (as we all are), as we reflect on his prolific international career (and with a plethora of records to be broken over the next decade) one must look back at the CB series knock that changed it all. On that fateful night at Hobart, Kohli had not only kept his team in contention, he had actually dragged a drained Indian side out of the airport. That night, at the Bellerive Oval, Virat Kohli transcended into a league of his own to etch his name in history - and a cricketing superstar was born. <br/><br/> <b>IPL through the years</b> <br/><br/> Ahead of the 2019 edition of the Indian Premier League (IPL), Virat Kohli showed how much faith he had in the franchise by declaring that he would perhaps end his career with the Bangalore-based Royal Challengers. The only player to be a part of a single franchise for the entire duration of the tournament (right from the start of the cash-rich league in 2008), Kohli has developed an affection with the franchise and with the fans over the period of time.  <br/><br/> Having been brought into the franchise as a young emerging player in 2008, Kohlis growth has been stupendous. He learnt under the wings of Rahul Dravid and Anil Kumble, before finally establishing himself under Daniel Vettori. It wasnt a free-flowing start, in a team that was struggling to find the essence of the tournament, it wasnt a surprise that they had a struggling youngster in the midst. Having learnt the ropes in the first three-year cycle, it wasnt a surprise that he was the only player retained in 2011. The purple patch began somewhere around that region, he then proved it wasnt just a purple patch, it was a career that was beginning to flourish. Soon after, Kohli became the best in all aspects, not just white-ball cricket, but in the red-ball version as well. <br/><br/> It became a no-brainer when he was asked to captain the Bangalore franchise on a permanent basis from 2012 and it also translated into more consistency with the bat. Kohli soon turned into a fan favourite even as runs flowed from his bat and eventually becoming the leading-run scorer in the history of IPL. Circa, 2016 - the India and RCB captain blasted 973 runs - the most by any player in the history of the game and it included four hundreds - the most by a batsman in a single edition.  Alas, all this didnt translate into a title triumph - one that has kept Kohli and Bangalore waiting so far (As of March 2023). <br/><br/> Written by <b>Rishi Roy</b>",
        #     "rankings": {
        #         "bat": [
        #             {
        #                 "odiRank": "3",
        #                 "testBestRank": "1",
        #                 "odiBestRank": "1",
        #                 "t20BestRank": "1"
        #             }
        #         ],
        #         "bowl": [
        #             {
        #                 "testBestRank": "0",
        #                 "odiBestRank": "0",
        #                 "t20BestRank": "89"
        #             }
        #         ],
        #         "all": [
        #             {}
        #         ]
        #     },
        #     "appIndex": {
        #         "seoTitle": "Virat Kohli Profile - Cricbuzz | Cricbuzz.com",
        #         "webURL": "http://www.cricbuzz.com/profiles/1413/virat-kohli"
        #     },
        #     "DoBFormat": "November 05, 1988",
        #     "faceImageId": "332891"
        # }

        # return response

     ################               END      ################################
