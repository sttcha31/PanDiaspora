/** @type {import('next').NextConfig} */
const nextConfig = {
    webpack: (config, { isServer }) => {
        // Add your custom loader for CSV files
        config.module.rules.push({
          test: /\.csv$/,
          use: [
            {
              loader: 'csv-loader',
              options: {
                // Add any CSV loader options here if needed
              },
            },
          ],
        });
    
        // Important: Return the modified config
        return config;
      },  
}

module.exports = nextConfig
