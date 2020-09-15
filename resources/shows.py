from flask_restful import Resource, reqparse
from models.shows import ShowsModel
from scraper import main_df

class Show(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lst', type=str, action='append')

    def get(self, imdb_key):
        shows = ShowsModel.find_by_imdb_key(imdb_key)
        if shows:
            return shows.json()
        return {'message': 'Item not found'}, 404

    def post(self, imdb_key):
        to_scrape = Show.parser.parse_args()["lst"]
        print(to_scrape)
        somelist = [x for x in to_scrape if not ShowsModel.find_by_imdb_key(x)]

        #check if list is empty    
        if len(somelist)==0:
             return {"message": "All the items are in database already"}, 201
        else:    
            #dict of id and episodes:
            parsed_data = main_df(to_scrape)  
            
            #loop over dict to add every item to database
            for key in parsed_data:
                item = ShowsModel(key, parsed_data[key])    
                try:
                    item.save_to_db()
                except:
                    return {"message": "An error occurred inserting the item."}, 500

            return parsed_data, 201

    def delete(self, imdb_key):
        show = ShowsModel.find_by_imdb_key(imdb_key)
        if show:
            show.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404


class ShowsList(Resource):
    def get(self):
        return {'Shows': [x.json() for x in ShowsModel.find_all()]}