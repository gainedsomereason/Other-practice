package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

}
/**
 * ssh
 * 指令：ssh-keygen -t rsa -b 4096 -C "happy-yan"
 * Generating public/private rsa key pair.
 * Enter file in which to save the key (/c/Users/10055/.ssh/id_rsa):
 * 
 * 
 */
//$ ssh-keygen -t rsa -b 4096 -C "happy-yan"
//Generating public/private rsa key pair.
//Enter file in which to save the key (/c/Users/10055/.ssh/id_rsa):
//Created directory '/c/Users/10055/.ssh'.
//Enter passphrase for "/c/Users/10055/.ssh/id_rsa" (empty for no passphrase):
//Enter same passphrase again:
//Your identification has been saved in /c/Users/10055/.ssh/id_rsa
//Your public key has been saved in /c/Users/10055/.ssh/id_rsa.pub
//The key fingerprint is:
//SHA256:YJtDuyLqcstA8dns1wT7R//oqSuho7cNe4DwwwURtMw happy-yan
//The key's randomart image is:
//+---[RSA 4096]----+
//|    .+o          |
//|    o..          |
//| .   E=.         |
//|  o.+o *o        |
//| . o+oB.S. .     |
//|.   .= ++.. .    |
//|. . ..oooo.. .   |
//|.+.. ..++o.   +  |
//|+oo. .oo+..o++ . |
//+----[SHA256]-----+

/**
 * 新建仓库
 * git init
 * 克隆仓库
 * git clone git@gitee.com:MaybeLiuS/indicator-system.git
 * 如果文件非常大则
 * 
 * git clone git@gitee.com:MaybeLiuS/indicator-system.git --depth 10//只去pull最新十次的提交结果
 * 对于一些很久的分支，更新子模块
 * git submodule update --init --recursive//直接去git update得不到子模块的更新，而这个命令对子模块进行递归的更新
 * 查看状态，确认一下是否有一些没有track的子模块
 * git status
 * 
 * 提交人是谁
 * git config --global user.email "ohh"
 * git config --global user.name "haha"
 * 新手使用师兄留下的代码分支，又不能直接改
 * git checkout -b happy/0817_test//在师兄的分支里使用这个命令提交一个新的分支，分支名为0817_test，用日期当前缀，过几天就换个分支；或者在一个主分支上做维护，其他小分支修细节
 * 
 * git add xx.java将xx.java添加到暂存区(stage)
 * git reset xx.java从暂存区移除
 * 
 * git commit -m "[planner]:add st boundary pre decider test"添加评论
 * git push将本地的一个分支传到远端
 * git push --set-upstream origin happy/0817_test第一次将本地的这个分支传到远端，需要先在远端新建这样一个分支
 * 
 * git reset --soft HEAD^撤回
 * git push -f强制提交
 * 
 */
