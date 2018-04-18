# Script generated with Bloom
pkgdesc="ROS - Tests for roscpp which depend on rostest."
url='http://ros.org/wiki/roscpp'

pkgname='ros-lunar-test-roscpp'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pkg-config'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-cpp-common'
'ros-lunar-message-generation'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roscpp-serialization'
'ros-lunar-roscpp-traits'
'ros-lunar-rosgraph-msgs'
'ros-lunar-roslang'
'ros-lunar-rostest'
'ros-lunar-rostime'
'ros-lunar-rosunit'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-xmlrpcpp'
)

depends=('ros-lunar-message-runtime'
'ros-lunar-rosconsole'
'ros-lunar-rosgraph-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-xmlrpcpp'
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
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

