import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
	compress: true,
	reactStrictMode: true,
	generateEtags: true,
	skipMiddlewareUrlNormalize: true,
	poweredByHeader: false,
	productionBrowserSourceMaps: false,
	crossOrigin: 'use-credentials',
	typescript: {
		ignoreBuildErrors: true,
	},
	eslint: {
		ignoreDuringBuilds: true,
	},
	images: {
		remotePatterns: [
			{
				protocol: 'https',
				hostname: 't.me',
			},
		],
	},
}

export default nextConfig