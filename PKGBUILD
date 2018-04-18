# Script generated with Bloom
pkgdesc="ROS - Tests for roscpp which depend on rostest."
url='http://ros.org/wiki/roscpp'

pkgname='ros-kinetic-test-roscpp'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pkg-config'
'ros-kinetic-catkin>=0.5.68'
'ros-kinetic-cpp-common'
'ros-kinetic-message-generation'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-roscpp-traits'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-roslang'
'ros-kinetic-rostest'
'ros-kinetic-rostime'
'ros-kinetic-rosunit'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-xmlrpcpp'
)

depends=('ros-kinetic-message-runtime'
'ros-kinetic-rosconsole'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=test_roscpp
source=()
md5sums=()

prepare() {
    cp -R $startdir/test_roscpp $srcdir/test_roscpp
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

