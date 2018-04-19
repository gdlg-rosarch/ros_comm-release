# Script generated with Bloom
pkgdesc="ROS - rosparam contains the rosparam command-line tool for getting and setting ROS Parameters on the <a href="http://www.ros.org/wiki/Parameter%20Server">Parameter Server</a> using YAML-encoded files. It also contains an experimental library for using YAML with the Parameter Server. This library is intended for internal use only. rosparam can be invoked within a <a href="http://www.ros.org/wiki/roslaunch">roslaunch</a> file."
url='http://ros.org/wiki/rosparam'

pkgname='ros-melodic-rosparam'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
)

depends=('python2-yaml'
'ros-melodic-rosgraph'
)

conflicts=()
replaces=()

_dir=rosparam
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosparam $srcdir/rosparam
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

