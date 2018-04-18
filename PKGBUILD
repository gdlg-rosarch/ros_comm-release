# Script generated with Bloom
pkgdesc="ROS - roswtf is a tool for diagnosing issues with a running ROS system. Think of it as a FAQ implemented in code."
url='http://ros.org/wiki/roswtf'

pkgname='ros-kinetic-roswtf'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.68'
'ros-kinetic-cmake-modules'
'ros-kinetic-rostest'
)

depends=('python2-paramiko'
'python2-rospkg'
'ros-kinetic-rosbuild'
'ros-kinetic-rosgraph'
'ros-kinetic-roslaunch'
'ros-kinetic-roslib'
'ros-kinetic-rosnode'
'ros-kinetic-rosservice'
)

conflicts=()
replaces=()

_dir=roswtf
source=()
md5sums=()

prepare() {
    cp -R $startdir/roswtf $srcdir/roswtf
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

