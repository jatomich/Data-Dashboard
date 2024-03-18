table_list = [
    {
        'netflix_titles': "CREATE TABLE netflix_titles ( \
            `netflix_id` int(11) NOT NULL AUTO_INCREMENT, \
            `type` varchar(100), \
            `title` varchar(100), \
            `director` varchar(100), \
            `cast` varchar(100), \
            `country` varchar(100), \
            `date_added` varchar(8), \
            `release_year` int(4), \
            `rating` varchar(10), \
            `duration` varchar(20), \
            `listed_in` varchar(250), \
            `description` varchar(512), \
            PRIMARY KEY (`kagglenetflix_id`), UNIQUE KEY `title, release_year` (`title`, `release_year`) \
        ) \
            ENGINE=InnoDB"
    },
    {
        'netflix_dump': "CREATE TABLE netflix_dump ( \
            `netflixdump_id` int(11) NOT NULL AUTO_INCREMENT, \
            'title': varchar(100), \
            'available globally?': varchar(100), \
            'release_year': varchar(4), \
            'hours viewed': varchar(100), \
            PRIMARY_KEY (`netflixdump_id`), UNIQUE KEY `title, release_year` (`title`, `release_year`) \
        ) \
            ENGINE=InnoDB"
    },
    {
        'netflix_combined': "CREATE TABLE netflix_combined ( \
            `netflix_id` int(11) NOT NULL AUTO_INCREMENT, \
            `showID` varchar(20), \
            `title` varchar(100), \
            `type` varchar(100), \
            `director` varchar(100), \
            `cast` varchar(100), \
            `country` varchar(100), \
            `releaseYear` int(4), \
            `mpaaRating` varchar(10), \
            `dateAdded` varchar(8), \
            `listed_in` varchar(250), \
            `duration` varchar(20), \
            `description` varchar(512), \
            `available_globally?': varchar(5), \
            `hours_viewed`: int(20) \
            PRIMARY KEY (`kagglenetflix_id`), UNIQUE KEY `title, release_year` (`title`, `release_year`) \
        ) \
            ENGINE=InnoDB"
    },
    {
        'imdb_titles': "CREATE TABLE imdb_titles ( \
            `imdbtitles_id` int(11) NOT NULL AUTO_INCREMENT, \
            `tconst` varchar(10), \
            `titleType` varchar(50), \
            `primaryTitle` varchar(250), \
            `originalTitle` varchar(250), \
            `isAdult` int(1), \
            `startYear` int(4), \
            `endYear` int(4), \
            `runtimeMinutes` int(10), \
            `genres` varchar(250), \
            PRIMARY KEY (`imdb_id`), UNIQUE KEY `primaryTitle, startYear` (`title`, `startYear`) \
        ) \
            ENGINE=InnoDB"
    },
    {
        'imdb_ratings': "CREATE TABLE imdb_ratings ( \
            `imdbratings_id` int(11) NOT NULL AUTO_INCREMENT, \
            'tconst': varchar(10), \
            'averageRating': varchar(4), \
            'numVotes': varchar(10), \
            PRIMARY_KEY (`imdbratings_id`), UNIQUE KEY `tconst` (`tconst`) \
        ) \
            ENGINE=InnoDB"
    },
    {
        'imdb_combined': "CREATE TABLE imdb_combined ( \
            `imdbcombined_id` int(11) NOT NULL AUTO_INCREMENT, \
            `tconst` varchar(10), \
            `titleType` varchar(50), \
            `primaryTitle` varchar(250), \
            `originalTitle` varchar(250), \
            `isAdult` int(1), \
            `startYear` int(4), \
            `endYear` int(4), \
            `runtimeMinutes` int(10), \
            `genres` varchar(250), \
            `averageRating`: varchar(4), \
            `numVotes`: varchar(10), \
            PRIMARY KEY (`imdbcombined_id`), UNIQUE KEY `primaryTitle, startYear` (`title`, `startYear`) \
        ) \
            ENGINE=InnoDB"
    }
]