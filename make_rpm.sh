#! /bin/sh

mkdir -p RPMS
mkdir -p SRPMS
mkdir -p BUILDROOT
mkdir -p BUILD
rpmbuild -ba SPECS/python26-xapi-libs.spec 
