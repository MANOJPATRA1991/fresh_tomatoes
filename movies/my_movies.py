"""This module defines functions to write data related to movies to fresh_tomatoes.html file."""
import webbrowser
import os
import re

# Styles and scripting for the page
MAIN_PAGE_HEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background: url(https://images2.alphacoders.com/141/141340.jpg) top right no-repeat;
            background-attachment:fixed;
            background-position: center;
            background-size: cover;
            background-color: #585858;
        }
        
        blockquote{
            font-size: 1.5em;
        }

        span{
            color: green;
            padding-right: 10px;
            text-align: justify;
        }

        .rate{
            padding-right: 50px;
            display: inline-block;
        }

        .rate h3{
            text-align: center;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 1280px;
            height: 720px;
        }

        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }

        #trailer-video {
            width: 100%;
            height: 100%;
        }

        #movie-rev{
            height: 150px;
            overflow-y: auto;
        }
        
        /*modified scrollbar for use in div with id movie-rev*/
        #movie-rev::-webkit-scrollbar {
            width: 1em;
        }
 
        #movie-rev::-webkit-scrollbar-track {
            -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
        }
 
        #movie-rev::-webkit-scrollbar-thumb {
          background-color: darkgrey;
          outline: 1px solid slategrey;
        }

        #movie-detail p{
            color: red;
        }

        .movie-tile {
            position:relative;
            margin-bottom: 20px;
            padding-top: 20px;
            transition: transform 1s;
        }
        
        .movie-tile:hover {
            cursor: pointer;
            transform: scale(1.2)
        }

        .caption{
            position: absolute;
            height: 342px;
            width: 220px;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            border-radius: 0;
            background:#000;
            background: -webkit-linear-gradient(bottom, #000 40%, rgba(0, 0, 0, 0) 100%) repeat scroll 0 0 rgba(0, 0, 0, 0);
            background: -moz-linear-gradient(bottom, #000 40%, rgba(0, 0, 0, 0) 100%) repeat scroll 0 0 rgba(0, 0, 0, 0);
            background: -o-linear-gradient(bottom, #000 40%, rgba(0, 0, 0, 0) 100%) repeat scroll 0 0 rgba(0, 0, 0, 0);
            background: linear-gradient(to top, #000 40%, rgba(0, 0, 0, 0) 100%) repeat scroll 0 0 rgba(0, 0, 0, 0);
            text-align: center;
            visibility: hidden;
            opacity: 0;
            transition: opacity .2s, visibility .2s;
        }

        .thumbnail{
            position: relative;
            width: 220px;
            height: 342px;
            border-radius: 0;
            border: 0 none;
            box-shadow: none;
        }

        .thumbnail > img{
            height: 100%;
            width:100%;
        }

        .movie-tile .caption h2,p{
            color: #fff;
            padding-top: 10px;
        }

        .movie-tile:hover .caption{
            visibility: visible;
            opacity:0.9;
        }

        .scale-media {
            padding-bottom: 65.25%;
            position: relative;
        }

        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 15px;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
            $("#movie-detail").empty();
            $("#movie-reviews").empty();
        });
        
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var genre = $(this).attr('data-genre');
            var rev = eval($(this).data('reviews'));
            var revr = eval($(this).data('reviewers'));
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            var rating=$(this).attr('data-rating');
            var imdb = $(this).attr('data-imdb');
            var rt = $(this).attr('data-rt');
            var cast = eval($(this).data('cast'));
            var director = $(this).attr('data-director');
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'allowfullscreen': "",
              'src': sourceUrl,
              'frameborder': 0
            }));
            $("#movie-detail").empty().append($('<h3><img src="https://blog.majestic.com/wp-content/uploads/2010/10/Video-Icon-crop-300x225.png" width="60" height="40">  ' + rating + '</h3>' +
                                                '<div class="rate"><h3> ' + imdb + '</h3><p>IMDB </p></div>' +
                                                '<div class="rate"><h3> ' + rt + '</h3><p>Rotten Tomatoes </p></div><hr/>' +
                                                '<div class="rate"><h2>Genre </h2><p><span>' + genre + '</span></p></div><hr/>' +
                                                '<div><h2>Cast </h2><p> '));
            $.each(cast, function(i, val){
                $("#movie-detail").append($('<span>' + val + ' |</span>'));
            });
            $("#movie-detail").append($('</p></div><hr/><div class="rate"><h2>Director </h2><p><span> ' + director + '</span></p></div>'));
            $("#movie-reviews").empty().append($('<hr/><h2> Reviews </h2><div id="movie-rev">'));
            $.each(revr, function(i, val){
                $("#movie-rev").append($('<blockquote><h4>' + rev[i] + '</h4><footer><cite><em>' + val + '</em></cite></footer></blockquote>'));
            });
            $("#movie-rev").append($('</div></div>'));
        });
        
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
"""


# The main page layout and title bar
MAIN_PAGE_CONTENT = """
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
            <div class="row">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                </a>
                <div class="row col-xs-9">
                    <!--youtube media player-->
                    <div class="row col-xs-12">
                        <div class="scale-media" id="trailer-video-container">
                        </div>
                    </div>
                </div>
                <!--to display additional info for a movie-->
                <div class="col-xs-3" id="movie-detail">
                </div>
                <!--contains reviews for a movie-->
                <div class="col-xs-12">
                    <div class="col-xs-12" id="movie-reviews">
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
"""


# A single movie entry html template
MOVIE_TILE_CONTENT = """
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-rating="{mpaa_rating}"
 data-imdb="{imdb}" data-rt="{rt}" data-cast="{cast}" data-director="{director}" data-genre="{genre}"
 data-reviews="{reviews}" data-reviewers="{reviewers}" data-toggle="modal" data-controls-modal="modal" data-target="#trailer" data-backdrop="static" data-keyboard="false">
    <div class="thumbnail">
        <img src="{poster_image_url}" width="220" height="342">
    
        <div class="caption"><h2>{movie_title}</h2><p><br>{movie_storyline}</p></div>
    </div>    
</div>
"""


def create_movie_tiles_content(movies):
    """
    This function creates movie tiles containing movie details 
    for each item in the movies list

    Args:
        movies: A list object containing instances of class Movies

    Returns:
         A string which contains data for all the movie items.
    """
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        
        #extract the part following v=
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)

        #extract the part following be/
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)

        #youtube_id_match.group(0) returns the string extracted
        #based on regex from movie.trailer_youtube_url
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        
        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            genre=movie.genre,
            movie_storyline=movie.storyline,
            mpaa_rating=movie.mpaa_rating,
            imdb=movie.imdb,
            rt=movie.rotten_tomatoes,
            cast=movie.cast,
            director=movie.director,
            reviews=movie.reviews,
            reviewers=movie.reviewers
        )
    return content


def open_movies_page(movies):
    """
    This function takes a movies list object as an argument and 
    writes it at respective DOM location inside the fresh_tomatoes.html file.

    Args:
        movies: A list object containing instances of class Movies
    """
    # Create or overwrite the output file
    #Open file and return a corresponding file object
    output_file = open('fresh_tomatoes.html', 'w')      

    # Replace the movie tiles placeholder with generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    
    #close the file
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    
    #open in new tab if possible
    webbrowser.open('file://' + url, new=2)
