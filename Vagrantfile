def to_boolean(val)
    ['true', 'True', true, '1'].include? val
end

use_nfs = to_boolean ENV.fetch('USE_NFS', false)

Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.network :private_network, ip: "192.168.21.253"
    config.ssh.forward_agent = true

    # Share an additional folder to the guest VM. The first argument is the
    # folder on the host, second is the folder on the guest.
    config.vm.synced_folder "src/", "/opt/src", :nfs => use_nfs

    config.vm.provision :ansible do |ansible|
        ansible.playbook = "vagrant.yml"
        ansible.verbose = 'extra'
        ansible.inventory_path = "hosts"
        ansible.extra_vars = {use_nfs: use_nfs}
    end

end
