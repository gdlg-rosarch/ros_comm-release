# Script generated with Bloom
pkgdesc="ROS - XmlRpc++ is a C++ implementation of the XML-RPC protocol. This version is heavily modified from the package available on SourceForge in order to support roscpp's threading model. As such, we are maintaining our own fork."
url='http://xmlrpcpp.sourceforge.net'

pkgname='ros-lunar-xmlrpcpp'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('LGPL-2.1'
)

makedepends=('boost'
'ros-lunar-catkin'
'ros-lunar-cpp-common'
'ros-lunar-rostime>=0.6.9'
)

depends=('ros-lunar-cpp-common'
'ros-lunar-rostime>=0.6.9'
)

conflicts=()
replaces=()

_dir=xmlrpcpp
source=()
md5sums=()

prepare() {
    cp -R $startdir/xmlrpcpp $srcdir/xmlrpcpp
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

