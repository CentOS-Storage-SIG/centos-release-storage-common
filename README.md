centos-release-storage-common is a package shared between the different
projects of the CentOS Storage SIG. This package contains the public GPG key
that is used for verification of the released RPMs.

This package needs to get build against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)
 - core6-extras-common-el6.centos (tag: core6-extras-common-candidate)

Building the package can be done like this:


    $ rpmbuild -bs \
               --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" \
               --define "dist .el7.centos" \
               centos-release-storage-common.spec

    $ cbs \
           build core7-extras-common-el7.centos \
           centos-release-storage-common-2-2.el7.centos.src.rpm

