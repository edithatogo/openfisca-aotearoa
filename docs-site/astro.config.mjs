import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://edithatogo.github.io',
  base: '/openfisca-aotearoa/',
  integrations: [
    mdx(),
    sitemap(),
    starlight({
      title: 'OpenFisca Aotearoa',
      description: 'Legal NZ documentation portal for OpenFisca Aotearoa.',
      sidebar: [
        { label: 'Start', items: ['index', 'docs-tooling-audit'] },
      ],
    }),
  ],
});
