# Script generated with Bloom
pkgdesc="ROS - This is a set of tools for recording from and playing back ROS message without relying on the ROS client library."


pkgname='ros-melodic-rosbag-storage'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'bzip2'
'console-bridge'
'ros-melodic-catkin'
'ros-melodic-cpp-common>=0.3.17'
'ros-melodic-roscpp-serialization'
'ros-melodic-roscpp-traits>=0.3.17'
'ros-melodic-roslz4'
'ros-melodic-rostime'
)

depends=('boost'
'bzip2'
'console-bridge'
'ros-melodic-cpp-common>=0.3.17'
'ros-melodic-roscpp-serialization'
'ros-melodic-roscpp-traits>=0.3.17'
'ros-melodic-roslz4'
'ros-melodic-rostime'
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

