// Copyright (c) 2020, The OTNS Authors.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
// 3. Neither the name of the copyright holder nor the
//    names of its contributors may be used to endorse or promote products
//    derived from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.

package types

import "math"

type NodeId = int

const (
	MaxNodeId       NodeId = 0xffff
	InvalidNodeId   NodeId = 0
	BroadcastNodeId NodeId = -1
)

const (
	// InvalidExtAddr defines the invalid extended address for nodes.
	InvalidExtAddr uint64 = math.MaxUint64
)

type NodeMode struct {
	RxOnWhenIdle       bool
	SecureDataRequests bool
	FullThreadDevice   bool
	FullNetworkData    bool
}

func DefaultNodeMode() NodeMode {
	return NodeMode{
		RxOnWhenIdle:       true,
		SecureDataRequests: true,
		FullThreadDevice:   true,
		FullNetworkData:    true,
	}
}

func ParseNodeMode(s string) (mode NodeMode) {
	for _, c := range s {
		switch c {
		case 'r':
			mode.RxOnWhenIdle = true
		case 's':
			mode.SecureDataRequests = true
		case 'd':
			mode.FullThreadDevice = true
		case 'n':
			mode.FullNetworkData = true
		}
	}
	return
}

type AddrType string

const (
	AddrTypeAny       AddrType = "any"
	AddrTypeMleid     AddrType = "mleid"
	AddrTypeRloc      AddrType = "rloc"
	AddrTypeLinkLocal AddrType = "linklocal"
)
