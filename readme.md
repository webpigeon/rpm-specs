# RPM Specfiles
These are specfiles for building RPMs from. I've created these for my own personal use but feel free to use them if you want to. One day I'll put them in a copr repository or something.

## Building the RPMs
build these using rpmbuild

    # copy the specs to the place rpmbuild wants them to be
    mkdir -p ~/rpmbuild/SPECS
    cp specs/*.spec ~/rpmbuild/SPECS/

    # download the sources
    mkdir -p ~/rpmbuild/SOURCES
    cd ~/rpmbuild/SOURCES
    # wget url in source: of the spec

    # build the rpms
    cd ~/rpmbuild/SPECS
    rpmbuild -ba specfilename.spec

this will put the binary rpm in ~/rpmbuild/RPMS/ and the source RPM in ~/rpmbuild/SRPMs/

If you have any errors due to missing dependencies in the specfile, file an issue and I'll fix it :).
