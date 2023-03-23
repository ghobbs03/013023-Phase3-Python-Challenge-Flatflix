class Review:
    
   def __init__(self, viewer, movie, rating):
        from .viewer import Viewer
        from .movie import Movie
        if (isinstance(viewer, Viewer)):
           self._viewer = viewer
        else:
           raise Exception('must be Viewer')
           
        if (isinstance(movie, Movie)):
           self._movie = movie
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
    

   def get_viewer(self):
      return self._viewer
   
   def set_viewer(self, viewer):
      self._viewer = viewer

   def get_movie(self):
      return self._movie
   
   def set_movie(self, movie):
      self._movie = movie


    # rating property goes here!
   rating = property(get_rating, set_rating)

    # viewer property goes here!
   viewer = property(get_viewer, set_viewer)

    # movie property goes here!
   movie = property(get_movie, set_movie)
