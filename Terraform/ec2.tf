data "aws_ami" "ubuntu" {

  most_recent = true

  owners = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

}
resource "aws_instance" "aeronexus" {

  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  subnet_id              = aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  key_name = var.key_name

  associate_public_ip_address = true
  user_data                   = file("${path.module}/userdata.sh")
  tags = {
    Name = "${var.project_name}-server"
  }


}