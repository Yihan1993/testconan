# Test Conan package 

## Content

This directory is a example for customized conan project

## Source from SCM

The conan package will be built from the sources thourgh git clone process

### Build Step

#### Automatic build conan package

> conan create . demo/testing

#### Manuell build conan package

Export the conan recipe from the user folder into the **local cache**
> conan export . demo/testing

Install the package with local recipe
> conan install add/0.1@demo/testing --build=missing

> conan test test_package add/0.1@demo/testing

Another possible way is to install the conan package from remote conan server (since the requirments is defined in test_package/conanfile.py)

> cd test_package && conan install .. --install_folder build/ --building=missing




