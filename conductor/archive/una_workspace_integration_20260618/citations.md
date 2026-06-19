# Citation Evidence

Track 16 is a workspace tooling track. The primary upstream sources reviewed
for the implementation decision were:

- <https://docs.astral.sh/uv/concepts/projects/workspaces/>
- <https://una.rdrn.me/>
- <https://una.rdrn.me/quickstart/>
- <https://una.rdrn.me/install/>
- <https://una.rdrn.me/build/>

The local implementation keeps this nested repository as a standalone uv
self-workspace and documents parent invocation through `uv --directory
openfisca-aotearoa`.
