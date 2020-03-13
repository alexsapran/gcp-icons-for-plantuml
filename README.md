# gcp-icons-for-plantuml

This is not official Google or Plantuml library. 

It downloads the official [Google icons](https://cloud.google.com/icons) and creates the required 
plantuml library components in order to allow easier integration.

## How build 

In order to use the latest version of the icons that Google provides please use the provided scripts 
that will download the icons and generate the required plantuml sprites.

Example 

``` shell
$ cd scripts
$ make download
# this will downloads the icons
$ make create_graphics
# this step will take some time to complete as it will go for each png and create the appropriate sprite
```
