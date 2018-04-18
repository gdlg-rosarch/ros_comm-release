# Script generated with Bloom
pkgdesc="ROS - ROS console output library."
url='http://www.ros.org/wiki/rosconsole'

pkgname='ros-lunar-rosconsole'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('apr'
'apr-util'
'boost'
'log4cxx'
'ros-lunar-catkin'
'ros-lunar-cpp-common'
'ros-lunar-rostime'
'ros-lunar-rosunit'
)

depends=('apr'
'apr-util'
'log4cxx'
'ros-lunar-cpp-common'
'ros-lunar-rosbuild'
'ros-lunar-rostime'
)

conflicts=()
replaces=()

_dir=rosconsole
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosconsole $srcdir/rosconsole
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

