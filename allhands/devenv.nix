{ pkgs, config, ... }:

{
  packages = [
    pkgs.git
    pkgs.zlib
  ];
  languages.python = {
    enable = true;
    poetry.enable = true;
  };
}
