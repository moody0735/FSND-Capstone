import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import setup_db, Actor, Movie





class AgencyTestCase(unittest.TestCase):
    """This class represents the test case"""
 
    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', '9520099', 'localhost:5432', self.database_name)
        setup_db(self.app)

     

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()



        self.actor = {
            "name" : "new actor added",
            "age" : "35",
            "gender" : "Male"
        }


        self.movie = {
            "title" : "new movie added",
            "release" : "2020"    
        }



        self.producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9mTlJma0gtcUpvRUMwUktjb0tLUyJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNTAzMGRhMWY2MDMwMDE5YjA4ZTNhIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTk3Njg4NTMzLCJleHAiOjE1OTc2OTU3MzMsImF6cCI6ImsydWMzbGFXejNhejMxd3p1eEVuU1RQb1VuNnhFVzFqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.wCgPBWtJ4-pAVYiCF0VfgeX8sq4YK9KS7gk01D8OPsAd04dM_ErINXrbNoWD0-DH_J_GK_XhdXHJenWxrMMHjd7UiW0blzAUMelit3WpxBuWPeM2RfMz1VcRNKcDq1Qp9Q41_0FpqVGANKY4zqvSe5g45Zg766DrhNhvUudPjprhFxjmqdcEU9k22tFFRKzYo1vRYAXLbAtZoqqaa2CBxsWHrBt9hxKZblh-EJ-irLBZoBocrR9hmTrHOsOCCZjeG9WzqlHkqUuYRgTkCvG6NvwcmJGS6Hvu2LdiNh_X2P8e8Y5SvkLuMw7UyCI6mEUZTn1D8Quhx98wIJoFk9Jz_w"
        self.director_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9mTlJma0gtcUpvRUMwUktjb0tLUyJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNTA1Y2RhMTViN2IwMDEzNjFlZTk4IiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTk3Njg4NjU0LCJleHAiOjE1OTc2OTU4NTQsImF6cCI6ImsydWMzbGFXejNhejMxd3p1eEVuU1RQb1VuNnhFVzFqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9ycyJdfQ.QWMLSLSrpEh6YhUI65vguJkWQtVwcr2bt_PImecPxUGkmbWs-GbAYYOxCi_QRNKefIvldAkWCTS9CZmRZB7WWfnE-np8r6N3NgBS6un-oAhtXCRvXbYf2Ho6mm_y3h_ENL1NQTuLW2mU21lsfCk3LeTit4AzWqTMA8xkQZWDPZeeKEbTyXixyJ7-RK-itG0cuTzwk-X0WWVWZXaT8pH_I7e-6M4FCvZo6-ahIh1-tInPl0597_3BNuj9VvbRgVwT7J_2HU5q4ink80kgiXps60iIeBugO5Vvp9llpGvg3pkpeOeWggVsshH7L2GiF5nMmTcM5cVZ9PEjNvONSAiimg"
        self.assistant_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9mTlJma0gtcUpvRUMwUktjb0tLUyJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzMzM2NzMzYWNkMGUwMDNhMWEwYzExIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNTk3Njg4Nzg2LCJleHAiOjE1OTc2OTU5ODYsImF6cCI6ImsydWMzbGFXejNhejMxd3p1eEVuU1RQb1VuNnhFVzFqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.q_MlonLgNDBmfBk7sfdDlk5iRDfNU0nm58eNdn6eVjMSe6IBoYPFjRrIFdzeelifcMUP7DObiSIO4Wg65Yv4gT8i0A_7rf1ffu6xcTu5a4MMfUHdnvDHSlAzpuRyVoa3OxpS1LxIFM9pafdAnx2P55Rkj3qC_k4qClg3IYQcdOHNsUzDAVt-9S4SU8fGhAME0y8cQ-XilMW0mZuTEcS5DSVgyWne2KLXug6e4ug7VhTqnknsBh27o3hARRcQYHd5tt5mCmXe9TnDYZYumSihDH3nZRGbm3yn-qALPDPfC7Lm_PE7Id8gTQJHxG2etkG8Qtl8aEDmYJMmfl9SegpuuA"



    def tearDown(self):
        """Executed after reach test"""
        pass
    

    
    
    # Test for return actors
    def test_get_actors(self):
    
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['actors'])
        self.assertEqual(data['success'], True)


    ''''

    # Test for return movies
    def test_get_movies(self):
    
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['movies'])
        self.assertEqual(data['success'], True) 




    # ---------------------------------------------------------
    # Director Role
    # ---------------------------------------------------------

    # Test for post new actor 
    def test_01_add_actor(self):

        response = self.client().post("/actors", json=self.actor, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)



    # Test for unsuccessful post empty actor 
    def test_02_uncreated_actor(self):
        request_data = {
            'name': '',
            'age': '',
        }
         
        response = self.client().post("/actors", json=request_data, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')



    # Test for patch actor 
    def test_03_edit_actor_by_ID(self):

        edited_actor = {
           'name': 'edited name'
        }

        response = self.client().patch('/actors/1', json=edited_actor, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


  

    # Test for delete actor 
    def test_04_delete_actor_by_ID(self):
        new_actor = Actor(
            name='one for delete',
            age='40',
            gender='female'
        )

        new_actor.insert()
        response = self.client().delete('/actors/{}'.format(new_actor.id), headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    # Test for delete an actor does not exist
    def test_05_delete_actor(self):
        response = self.client().delete('/actors/1000', headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    # Test for post new movie 
    def test_06_add_movie(self):

        response = self.client().post("/movies", json=self.movie, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')





    # Test for patch movie 
    def test_07_edit_movie_by_ID(self):

        edited_movie = {
           'title': 'edited title'
        }

        response = self.client().patch('/movies/1', json=edited_movie, headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)




 
    # Test for delete movie 
    def test_08_delete_movie_by_ID(self):
        new_movie = Movie(
            title='one for delete',
            release='2020'
        )

        new_movie.insert()
        response = self.client().delete('/movies/{}'.format(new_movie.id), headers={"Authorization":"Bearer {}".format(self.director_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')

    
    





    # ---------------------------------------------------------
    # Prdoucer Role
    # ---------------------------------------------------------

    # Test for post new actor 
    def test_09_add_actor(self):

        response = self.client().post("/actors", json=self.actor, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)



    # Test for unsuccessful post empty actor 
    def test_010_uncreated_actor(self):
        new_request_data = {
            'name': '',
        }
         
        response = self.client().post("/actors", json=new_request_data, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')



    # Test for patch actor 
    def test_011_edit_actor_by_ID(self):

        new_edited_actor = {
           'name': 'new edited name'
        }

        response = self.client().patch('/actors/1', json=new_edited_actor, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


  

    # Test for delete actor 
    def test_012_delete_actor_by_ID(self):
        new_actor = Actor(
            name='one for delete',
            age='40',
            gender='female'
        )

        new_actor.insert()
        response = self.client().delete('/actors/{}'.format(new_actor.id), headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    # Test for delete an actor does not exist
    def test_013_delete_actor(self):
        response = self.client().delete('/actors/1000', headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    # Test for post new movie 
    def test_014_add_movie(self):

        response = self.client().post("/movies", json=self.movie, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 200)


      


    # Test for unsuccessful post empty movie
    def test_015_uncreated_movie(self):
        request_data = {
            'title': '',
        }
         
        response = self.client().post("/movies", json=request_data, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')



    # Test for patch movie 
    def test_016_edit_movie_by_ID(self):

        edited_movie = {
           'title': 'edited title'
        }

        response = self.client().patch('/movies/1', json=edited_movie, headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)




 
    # Test for delete movie 
    def test_016_delete_movie_by_ID(self):
        new_movie = Movie(
            title='one for delete',
            release='2020'
        )

        new_movie.insert()
        response = self.client().delete('/movies/{}'.format(new_movie.id), headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    
    # Test for delete a movie does not exist
    def test_017_delete_movie(self):
        response = self.client().delete('/movies/1000', headers={"Authorization":"Bearer {}".format(self.producer_token)})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')



    # ---------------------------------------------------------
    # Assistant Role
    # ---------------------------------------------------------

    # Test for unauthorized post new actor 
    def test_018_add_actor(self):

        response = self.client().post("/actors", json=self.actor, headers={"Authorization":"Bearer {}".format(self.assistant_token)})
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')



    # Test for unauthorized patch movie 
    def test_019_edit_movie_by_ID(self):

        edited_movie = {
           'title': 'edited title'
        }

        response = self.client().patch('/movies/1', json=edited_movie, headers={"Authorization":"Bearer {}".format(self.assistant_token)})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission Not found')

    '''
    




    
    


    


   


    
   

    


    









    


 


    



    




      




    







  



     
 



        

        



