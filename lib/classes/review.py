class Review:
    
   def __init__(self, viewer, movie, rating):
        from .viewer import Viewer
        from .movie import Movie
        if (isinstance(viewer, Viewer)):
           self.viewer = viewer
        else:
           raise Exception('must be Viewer')
           
        if (isinstance(movie, Movie)):
           self.movie = movie
        else:
           raise Exception('must be Movie')
        if (type(rating) == int and 1 <= rating <= 5):
           self._rating = rating
        else:
           raise Exception('must be integer from 1 to 5')
        
        movie.add_review(self)
        viewer.add_review(self)
        viewer.add_movie(movie)
        

   
   def get_rating(self):
      return self._rating
   
   def set_rating(self, rating):
      if (type(rating) == int and 1 <= rating <= 5):
         self._rating = rating
    

    # rating property goes here!
   rating = property(get_rating, set_rating)

    # viewer property goes here!

    # movie property goes here!
