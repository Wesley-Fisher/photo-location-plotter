# photo-location-plotter

![Testing](https://github.com/Wesley-Fisher/photo-location-plotter/workflows/CI/badge.svg)

This is a small project that came out of a family project I worked on. It's purpose is to go through photos in a directory on your computer, and plot their GPS locations on a given map. The result is a map picture that highlights the locations of all the pictures - this approach was perfect for a map of a family vacation a few years ago:

![Pictures taken on vacation](.github/media/hawaii_pic.png)


# How to Use

1.  Install Requirements
2.  Create a folder for your 'project'
3.  Download a map file as an image
4.  Create a settings file
5.  Run


## Requirements

First of all, this code will need to be downloaded.

This code works using Python, and is tested on versions 3.5-3.9 on both Windows and Ubuntu. On both of these operating systems, you can open a command prompt, and run `pip install -r pip3_requirements.txt` in this directory. This should install all of the code needed.

You can run the command `python run.py test_project` in this directory to run tests and ensure everything is installed. If it works, you will see a `map_out.png` file under `projects/test_project/`


## Folder

The term for each map image you would like to create is a project. These are stored as folders in the 'projects' directory. Create a folder there. The name should:

1. Be easy to type/use, such as `family_vacation_2010`. You will need to enter the name in other locations.
2. Not contain spaces. Underscores make a good replacement. Avoid special characters.

## Download a Map File

You will need to download an image to serve as your map background. The trick to this is that you must know the GPS bounds (maximum and minimum latitude and longitude) of the map. Save these values.

OpenStreetMap currently (as of Jan 2021) has Both a 'Share' and an 'Export' function. Export can be used to select an area with GPS bounds displayed. You can then Share an area, select the 'Set custom dimensions' option, and align the regions.

## Create a Settings File

Within the directory you created, create a file called `config.yaml`. This file will tell the program information that is needed.

The current (as of Jan 2021) file for `test_project` is:

```
photo_directories:
 - $PROJECT/photos

map:
  in_file: map.png
  bounds:
    latitude: [44.67074, 44.67454]
    longitude: [-63.56463, -63.56199]
  out_file: map_out.png
styling:
  point_size: 35
  point_color: 'b'
  point_alpha: 0.5
regions:
  include_regions:
    - some_name:
      longitude: [-63.56463, -63.56199]
      latitude: [44.67074, 44.67454]
  exclude_regions:
    - some_name:
      longitude: [-63.56463, -63.564]
      latitude: [44.67074, 44.67454]
```

You will need to fill out the values for your project. The meaning of each of these is below. Items which are included in another (below and indented) are typed with /'s.

* map: data on the map file to use.
  * photo_directories: directories to find images files to use. If you type in $PROJECT, the path will start with the project folder. Otherwise, enter a full path. There can be more than one directory, each on it's own line, with a - preceding it.
  * in_file: the filename of the map image file you downloaded. Currently only a png has been tested, but other formats should work.
  * bounds: the bounding GPS coordinates of the map.
    * latitude: the minimum and maximum latitude values covered by the map.
    * longitude: the minimum and maximum longitude values covered by the map. More testing is needed, but if the map crosses the 0-degree line, these should correspond to 'left' and 'right' boundaries.
  * out_file: the filename of the map to be created. Make it different than the in_map, so it does not get overwritten.

* styling: information on how to color points
  * point_size: the size of points to draw on the map
  * point_color: the color of points to draw. 'b' is blue.
  * alpha: the opacity of points to draw. 0 is clear, while 1 is opaque.

* regions: these are regions that you want to include or exclude from the map, for whatever reason. Both include_regions and exclude_regions take on the same form in the file. You can include lists of multiple regions. Each must have one line that gives a name, starting with a -, and following lines giving latitude and longitude bounds.

  * include: GPS points _must_ lie within one of these regions to be included. All other points will be excluded.
  * exclude: any GPS point in _any_ of these regions will be excluded.

    * a name: some simple name to remember what this region is. Ignored by the program. Does not need to be 'a name' or 'some_name'.
    * latitude: minimum and maximum latitudes of the region
    * longitude: minimum and maximum longitudes of the region

## Run

In a command prompt, run `python run.py your_project_name_here`. If you also (still) have a python2 version installed, you may need to use `python3` instead.

You should see an image generated in your project folder with points plotted.