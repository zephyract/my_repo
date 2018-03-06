#!/bin/bash -eux
# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); # you may not use this file except in compliance with the License.  # You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################

LLVM_DEP_PACKAGES="build-essential make cmake ninja-build git subversion python2.7 binutils-gold binutils-dev"
apt-get install -y $LLVM_DEP_PACKAGES

# Checkout

# Use chromium's clang revision
SRC="/home/ubuntu/SRC"
mkdir $SRC/chromium_tools
cd $SRC/chromium_tools
# git clone https://chromium.googlesource.com/chromium/src/tools/clang
git clone https://gitee.com/M4x/google-clang.git clang
cd clang

LLVM_REVISION=$(grep -Po "CLANG_REVISION = '\K\d+(?=')" scripts/update.py)
echo "Using LLVM revision: $LLVM_REVISION"

# cd $SRC && git clone http://llvm.org/git/llvm.git
cd $SRC && git clone https://gitee.com/M4x/llvm.git
# cd $SRC/llvm/tools && git clone http://llvm.org/git/clang.git 
cd $SRC/llvm/tools && git clone https://gitee.com/M4x/clang.git
# cd $SRC/llvm/projects && git clone http://llvm.org/git/compiler-rt.git
cd $SRC/llvm/projects && git clone https://gitee.com/M4x/compiler-rt.git
# cd $SRC/llvm/projects && git clone http://llvm.org/git/libcxx.git
cd $SRC/llvm/projects && git clone https://gitee.com/M4x/libcxx.git
# cd $SRC/llvm/projects && git clone http://llvm.org/git/libcxxabi.git 
cd $SRC/llvm/projects && git clone https://gitee.com/M4x/libcxxabi.git

# Build & install
WORK="/home/ubuntu/WORK"
mkdir -p $WORK/llvm
cd $WORK/llvm
cmake -G "Ninja" \
      -DLIBCXX_ENABLE_SHARED=OFF -DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=ON \
      -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD="X86" \
      -DLLVM_BINUTILS_INCDIR=/usr/include $SRC/llvm
ninja
ninja install
rm -rf $WORK/llvm

mkdir -p $WORK/msan
cd $WORK/msan
cmake -G "Ninja" \
      -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ \
      -DLLVM_USE_SANITIZER=Memory -DCMAKE_INSTALL_PREFIX=/usr/msan/ \
      -DLIBCXX_ENABLE_SHARED=OFF -DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=ON \
      -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD="X86" \
      $SRC/llvm
ninja cxx
ninja install-cxx
rm -rf $WORK/msan

# Pull trunk libfuzzer.
# cd $SRC && git clone https://chromium.googlesource.com/chromium/llvm-project/llvm/lib/Fuzzer libfuzzer
cd $SRC && git clone https://gitee.com/M4x/Fuzzer.git libfuzzer

cp $SRC/llvm/tools/sancov/coverage-report-server.py /usr/local/bin/

# Install LLVMgold into bfd-plugins
mkdir /usr/lib/bfd-plugins
cp /usr/local/lib/libLTO.so /usr/lib/bfd-plugins
cp /usr/local/lib/LLVMgold.so /usr/lib/bfd-plugins

# Cleanup
rm -rf $SRC/llvm
rm -rf $SRC/chromium_tools
apt-get remove --purge -y $LLVM_DEP_PACKAGES
apt-get autoremove -y
