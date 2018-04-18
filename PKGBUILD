# Script generated with Bloom
pkgdesc="ROS - This is a set of tools for recording from and playing back ROS message without relying on the ROS client library."


pkgname='ros-kinetic-rosbag-storage'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'bzip2'
'console-bridge'
'ros-kinetic-catkin'
'ros-kinetic-cpp-common>=0.3.17'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-roscpp-traits>=0.3.17'
'ros-kinetic-roslz4'
'ros-kinetic-rostime'
)

depends=('boost'
'bzip2'
'console-bridge'
'ros-kinetic-cpp-common>=0.3.17'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-roscpp-traits>=0.3.17'
'ros-kinetic-roslz4'
'ros-kinetic-rostime'
)

conflicts=()
replaces=()

_dir=rosbag_storage
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosbag_storage $srcdir/rosbag_storage
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

