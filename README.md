Kalendas repository for Fedora and CentOS
=========================================

This website contains the repository of **kalendas**  for distros Linux based in RPM: *fedora* and *centos*.

Fedora
------
**kalendas** packages are available in versions 19, 20 and 21. First install the repository for to setup yum,
from the terminal run

    $ sudo yum install http://mikemolina.github.com/kalendas-rpm/kalendas-fedora-release-1.0-1.noarch.rpm
you will now be able to install the RPM package 

    $ sudo yum install kalendas

CentOS
------
**kalendas** is available for version 7. First install the repository for to setup yum, from the terminal run

    $ sudo yum install http://mikemolina.github.com/kalendas-rpm/kalendas-centos-release-1.0-1.noarch.rpm
install the RPM package by running

    $ sudo yum install kalendas

Building from the SRPM
----------------------
Need to install basic development tools

    $ sudo yum install @development-tools
    $ sudo yum install fedora-packager yum-utils

create the directory tree construction

    $ rpmdev-setuptree

download and install the SRPM package in ~/rpmbuild

    $ yumdownloader --source kalendas
    $ rpm -ivh kalendas-*.src.rpm
Next, build the rpm package

    $ rpmbuild -bb ~/rpmbuild/SPECS/kalendas.spec
the RPM are then available in ~/rpmbuild/RPMS/noarch. Now you can review and install

    $ rpmls ~/rpmbuild/RPMS/noarch/kalendas-*.noarch.rpm
    $ sudo rpm -ivp ~/rpmbuild/RPMS/noarch/kalendas-*.noarch.rpm
More information on RPM building in [How to create an RPM package](https://fedoraproject.org/wiki/How_to_create_an_RPM_package).
