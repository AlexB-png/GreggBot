# For use on nix-os
let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    # Python stuff
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.selenium
      python-pkgs.keyboard
      python-pkgs.requests
      python-pkgs.flask
      python-pkgs.schedule
      python-pkgs.pyngrok
    ]))

    # Other
    pkgs.firefox
    pkgs.nginx
  ];
}