package net.armagomen.battleobserver.battle.components.debugpanel
{
	import flash.display.Sprite;
	import flash.display.Bitmap;
	import mx.utils.StringUtil;
	import net.armagomen.battleobserver.utils.TextExt;
	import net.armagomen.battleobserver.utils.Filters;
	import flash.text.TextFieldAutoSize;
	
	public class modern extends Sprite
	{
		[Embed(source = "ping_img/0.png")]
		private var zero:Class;
		[Embed(source = "ping_img/1.png")]
		private var one:Class;
		[Embed(source = "ping_img/2.png")]
		private var two:Class;
		[Embed(source = "ping_img/3.png")]
		private var three:Class;
		[Embed(source = "ping_img/4.png")]
		private var four:Class;
		[Embed(source = "ping_img/5.png")]
		private var five:Class;
		[Embed(source = "ping_img/6.png")]
		private var sixth:Class;
		[Embed(source = "ping_img/7.png")]
		private var seven:Class;
		[Embed(source = "ping_img/8.png")]
		private var eight:Class;
		[Embed(source = "ping_img/9.png")]
		private var nine:Class;
		[Embed(source = "ping_img/10.png")]
		private var ten:Class;
		
		private var debugText:TextExt      = null;
		private const template:String      = "<textformat tabstops='[76, 160]'>FPS: <font color='{0}'>{1}</font><tab>PING: <font color='{2}'>{3}</font><tab><font color='{4}'>LAG</font></textformat>";
		
		private var fpsColor:String        = "#B3FE95";
		private var pingColor:String       = "#B3FE95";
		private var lagColor:String        = "#FD9675";
		private var icons:Vector.<Bitmap>  = null;
		private var lastVisibleIcon:Bitmap = null;
		
		public function modern(shadow_settings:Object, colors:Object)
		{
			super();
			this.debugText = new TextExt(20, 0, Filters.middleText, TextFieldAutoSize.LEFT, shadow_settings, this);
			this.fpsColor = colors.fpsColor;
			this.pingColor = colors.pingColor;
			this.lagColor = colors.pingLagColor;
			this.createBitmapVector();
		}
		
		private function createBitmapVector():void
		{
			this.icons = new Vector.<Bitmap>(11, true);
			
			var icon0:Bitmap = new zero();
			this.icons[0] = icon0;
			this.lastVisibleIcon = icon0;
			
			var icon1:Bitmap = new one();
			this.icons[1] = icon1;
			
			var icon2:Bitmap = new two();
			this.icons[2] = icon2;
			
			var icon3:Bitmap = new three();
			this.icons[3] = icon3;
			
			var icon4:Bitmap = new four();
			this.icons[4] = icon4;
			
			var icon5:Bitmap = new five();
			this.icons[5] = icon5;
			
			var icon6:Bitmap = new sixth();
			this.icons[6] = icon6;
			
			var icon7:Bitmap = new seven();
			this.icons[7] = icon7;
			
			var icon8:Bitmap = new eight();
			this.icons[8] = icon8;
			
			var icon9:Bitmap = new nine();
			this.icons[9] = icon9;
			
			var icon10:Bitmap = new ten();
			this.icons[10] = icon10;
			
			for each (var icon:Bitmap in this.icons)
			{
				icon.x = 15;
				icon.y = 25;
				icon.width = 210;
				icon.height = 7;
				icon.visible = false;
				icon.smoothing = true;
				this.addChild(icon);
			}
		}
		
		public function update(ping:int, fps:int, lag:Boolean):void
		{
			this.debugText.htmlText = StringUtil.substitute(this.template, this.fpsColor, fps, this.pingColor, ping, lag ? this.lagColor : this.pingColor);
			this.lastVisibleIcon.visible = false;
			
			if (ping < 10)
			{
				this.icons[10].visible = true;
				this.lastVisibleIcon = this.icons[10];
			}
			else if (ping < 20)
			{
				this.icons[9].visible = true;
				this.lastVisibleIcon = this.icons[9];
			}
			else if (ping < 30)
			{
				this.icons[8].visible = true;
				this.lastVisibleIcon = this.icons[8];
			}
			else if (ping < 40)
			{
				this.icons[7].visible = true;
				this.lastVisibleIcon = this.icons[7];
			}
			else if (ping < 50)
			{
				this.icons[6].visible = true;
				this.lastVisibleIcon = this.icons[6];
			}
			else if (ping < 70)
			{
				this.icons[5].visible = true;
				this.lastVisibleIcon = this.icons[5];
			}
			else if (ping < 100)
			{
				this.icons[4].visible = true;
				this.lastVisibleIcon = this.icons[4];
			}
			else if (ping < 150)
			{
				this.icons[3].visible = true;
				this.lastVisibleIcon = this.icons[3];
			}
			else if (ping < 200)
			{
				this.icons[2].visible = true;
				this.lastVisibleIcon = this.icons[2];
			}
			else if (ping < 800)
			{
				this.icons[1].visible = true;
				this.lastVisibleIcon = this.icons[1];
			}
			else
			{
				this.icons[0].visible = true;
				this.lastVisibleIcon = this.icons[0];
			}
		}
	}

}