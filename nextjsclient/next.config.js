// /** @type {import('next').NextConfig} */
// const nextConfig = {
//   reactStrictMode: true,
// }

// module.exports = nextConfig
module.exports = () => {
  const rewrites = () => {
    return [
      {
        source: "/upload/:path*",
        destination: "http://localhost:5000/upload/:path*",
      },
      {
        source: "/delete/:path*",
        destination: "http://localhost:5000/delete/:path*",
      },
      {
        source: "/read/:path*",
        destination: "http://localhost:5000/read/:path*",
      },
    ];
  };
  return {
    rewrites,
  };
};
