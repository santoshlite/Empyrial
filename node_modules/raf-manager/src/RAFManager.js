/**
 *  RAFManager requestAnimationFrame Manager
 * 
 *  Simple package
 * 
 *  CODE:
 * 
 * 		// Add to
 *  	-- RAFManager.add(func);
 * 
 *   	// Add and carry parameters
 *  	-- const func = data =>{ console.log(data) };
 *  	-- RAFManager.add(func, 25, { msg:'hello world!' }); 
 * 		
 * 		// remove
 *  	-- RAFManager.remove(func);
 *  	-- RAFManager.stop();	
*/

// simple polyfill by https://gist.github.com/paulirish/1579671
(function () {
	let lastTime = 0;
	let vendors = ['ms', 'moz', 'webkit', 'o'];
	for (let x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
		window.requestAnimationFrame = window[vendors[x] + 'RequestAnimationFrame'];
		window.cancelAnimationFrame = window[vendors[x] + 'CancelAnimationFrame']
			|| window[vendors[x] + 'CancelRequestAnimationFrame'];
	}
}());

const RAFManager = {
	timer: 0,
	state: 'stop',
	animations: [],

	add(callback, fps = 60, param = null) {
		const n = 60 / fps;
		const aniData = { callback, fps, n, param, i: 0 };
		this.animations.push(aniData);
		if (this.animations.length >= 1) this.start();

		return this;
	},

	getIndex(callback) {
		for (let i = 0; i < this.animations.length; i++) {
			const aniData = this.animations[i];
			if (aniData.callback === callback) return i;
		}

		return -1;
	},

	remove(callback) {
		const index = this.getIndex(callback);
		if (index < 0) return;

		this.deleteMap(callback);
		if (this.animations.length === 0) this.stop();

		return this;
	},

	deleteMap(callback) {
		const index = this.getIndex(callback);
		const aniData = this.animations[index];
		for (let key in aniData) delete aniData[key];

		this.animations.splice(index, 1);
	},

	start() {
		if (this.state === 'start') return;

		this.state = 'start';
		this.tick();
		return this;
	},

	stop() {
		if (this.state === 'stop') return;

		this.state = 'stop';
		cancelAnimationFrame(this.timer);
		return this;
	},

	tick() {
		this.timer = requestAnimationFrame(() => { this.tick(); });

		for (let i = 0; i < this.animations.length; i++) {
			const aniData = this.animations[i];
			const callback = aniData.callback;
			const param = aniData.param;

			aniData.i++;
			if (aniData.i >= aniData.n) {
				callback(param);
				aniData.i = 0;
			}
		}
	}
}

export default RAFManager;