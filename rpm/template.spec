%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-foxglove-bridge
Version:        0.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS foxglove_bridge package

License:        MIT
URL:            https://github.com/foxglove/ros-foxglove-bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       openssl
Requires:       ros-humble-ament-index-cpp
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-components
Requires:       ros-humble-rosgraph-msgs
Requires:       zlib-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  asio-devel
BuildRequires:  json-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-index-cpp
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-components
BuildRequires:  ros-humble-ros-environment
BuildRequires:  ros-humble-rosgraph-msgs
BuildRequires:  websocketpp-devel
BuildRequires:  zlib-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-std-srvs
%endif

%description
ROS Foxglove Bridge

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Feb 15 2023 John Hurliman <john@foxglove.dev> - 0.4.0-1
- Autogenerated by Bloom

* Wed Jan 04 2023 John Hurliman <john@foxglove.dev> - 0.3.0-1
- Autogenerated by Bloom

* Mon Dec 12 2022 John Hurliman <john@foxglove.dev> - 0.2.2-1
- Autogenerated by Bloom

* Mon Dec 05 2022 John Hurliman <john@foxglove.dev> - 0.2.1-1
- Autogenerated by Bloom

* Fri Dec 02 2022 John Hurliman <john@foxglove.dev> - 0.2.0-2
- Autogenerated by Bloom

* Thu Dec 01 2022 John Hurliman <john@foxglove.dev> - 0.2.0-1
- Autogenerated by Bloom

* Mon Nov 21 2022 Foxglove <contact@foxglove.dev> - 0.1.0-1
- Autogenerated by Bloom

