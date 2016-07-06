#!/bin/bash
export MAINDIR=$HOME/rpmbuild
export RPMDESC=$1
export RPMNAME=$2
export RPMVERSION=$3
export RPMRELEASE=$4

rpmbuild -v --target=noarch -bb --clean $MAINDIR/SPECS/tarpackage.spec 